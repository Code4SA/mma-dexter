(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // basic document view
  Dexter.DocumentView = function() {
    var self = this;

    self.placesSetup = false;

    self.init = function() {
      $('a[href="#places-tab"][data-toggle="tab"]').on('shown.bs.tab', self.onPlacesTabShown);

      var $text = $('.document-container .article-content');
      if ($text.length > 0) {
        $text.affix({
          offset: {
            top: $text.offset().top - 100,
          }
        });
      }

      $('.fixed-header')
        .affix({
          offset: {
            top: 55,
          }
        });

      // attachment viewer
      $('.attachment-list')
        .on('click', '.show-text', self.showArticleText)
        .on('click', '.attachment', self.showAttachment)
        .on('click', '.delete', self.deleteAttachment);

      return self;
    };

    self.showArticleText = function(e) {
      e.preventDefault();
      $('.article-content .article-text').show();
      $('.attachment-viewer').hide();
    }

    self.showAttachment = function(e) {
      e.preventDefault();
      var $attachment = $(this);

      $('.article-content .article-text').hide();
      $('.attachment-viewer').show();

      var map = self.getAttachmentMap();

      // ensure the attachment browser is visible
      $('.article-attachments').show();

      // remove existing layers
      map.eachLayer(function(l) { map.removeLayer(l); });

      var size = $attachment.data('size').split(',');
      var w = size[0],
          h = size[1];

      var southWest = map.unproject([0, h], map.getMaxZoom()-1);
      var northEast = map.unproject([w, 0], map.getMaxZoom()-1);
      var bounds = new L.LatLngBounds(southWest, northEast);

      map.setMaxBounds(bounds);
      map.setView([0, 0], map.getMaxZoom()-1);
      L.imageOverlay($attachment.data('url'), bounds).addTo(map);
    };

    self.deleteAttachment = function(e) {
      e.preventDefault();

      if (confirm('Really delete this attachment?')) {
        $(this).closest('li').remove();

        var attachments = $('.attachment-list li:not(.template) .attachment');
        if (attachments.length > 0) {
          attachments.first().click();
        } else {
          $('.article-attachments').hide();
        }
      }
    };

    self.getAttachmentMap = function() {
      if (!self.attachmentMap) {
        self.attachmentMap = L.map('attachment-slippy', {
          minZoom: 1,
          maxZoom: 4,
          zoom: 1,
          center: [0, 0],
          crs: L.CRS.Simple,
          attributionControl: false,
        });
      }

      return self.attachmentMap;
    };

    self.onPlacesTabShown = function(e) {
      // invalidate the map so that it gets resized correctly
      $($(this).attr('href') + ' .leaflet-container').each(function(i, map) {
        Dexter.maps.invalidate();
      });

      if (!self.placesSetup) {
        Dexter.maps.loadAndDrawPlaces();
        self.placesSetup = true;
      }
    };
  };

  // view when editing document details (NOT the analysis)
  Dexter.EditDocumentView = function() {
    var self = this;

    self.init = function() {
      if ($('#new-document, #edit-document').length === 0) {
        return;
      }

      $('button.submit').on('click', function(e) {
        $('#edit-document form').submit();
      });

      // author name autocomplete
      self.$authorName = $('#author-name');
      self.$authorWidget = $('.author-widget');

      self.authorHound = new Bloodhound({
        name: 'authors',
        remote: {
          url: '/api/authors?q=%QUERY',
          ajax: {
            beforeSend: function(xhr) {
              self.$authorName.addClass('spinner');
            }
          },
          filter: function(resp) {
            self.$authorName.removeClass('spinner');
            return resp.authors;
          },
        },
        sorter: function(a, b) {
          // compare on length, then alphabetically
          if (a.name.length == b.name.length) {
            return a.name.localeCompare(b.name);
          } else {
            return a.name.length - b.name.length;
          }
        },
        datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name); },
        queryTokenizer: Bloodhound.tokenizers.whitespace
      });
      self.authorHound.initialize();

      var autoset = false;

      self.$authorName.typeahead({
        minLength: 2,
        highlight: true,
        autoselect: true,
      }, {
        source: self.authorHound.ttAdapter(),
        displayKey: 'name',
      }).on('typeahead:selected', function(e, author, dataset) {
        autoset = true;
        self.setAuthor(author);
      }).on('typeahead:opened', function(e) {
        autoset = false;
      }).on('typeahead:closed', function(e) {
        if (!autoset) {
          // auto-select an exact match if we haven't already
          self.authorHound.get(self.$authorName.typeahead('val'), function(suggestions) {
            var needle = self.$authorName.typeahead('val').toLowerCase();

            for (var i = 0; i < suggestions.length; i++) {
              if (suggestions[i].name.toLowerCase() == needle) {
                // TODO: handle an exact match (eg. try 'sapa')
                self.$authorName.typeahead('val', suggestions[i].name);
                self.$authorName.typeahead('close');
                self.$authorName.trigger('typeahead:selected', [suggestions[i], null]);
                return;
              }
            }

            // new author
            self.setNewAuthor();
          });
        }
      });

      // dropzone for article attachments
      self.dropzone = new Dropzone("#dropzone", {
          url: '/articles/attachments',
          maxFilesize: 6,
          acceptedFiles: 'image/png,image/jpeg,image/gif,application/pdf',
          addRemoveLinks: true,
          headers: {"X-CSRF-Token": $('meta[name=csrf-token]').attr('content')},
        });
      self.dropzone
        .on('success', self.attachmentUploaded)
        .on('addedfile', function(e) { $('#dropzone .dz-preview:last-child').append('<i class="fa fa-spinner fa-spin fa-4x">'); });

      // show the first attachment, if any
      $('.attachment-list li:not(.template) .attachment').first().click();
    };

    self.attachmentUploaded = function(file) {
      // successfully uploaded
      self.dropzone.removeFile(file);

      var attachment = $.parseJSON(file.xhr.response).attachment;
      var li = $('.attachment-list .template')
        .clone()
        .removeClass('template')
        .appendTo($('.attachment-list'));

      $('<input type="hidden" name="attachments">')
        .val(attachment.id)
        .appendTo(li);

      $('a.download', li)
        .attr('href', attachment.download_url);

      $('img', li)
        .attr('src', attachment.thumbnail_url)
        .data('url', attachment.url)
        .data('size', attachment.size)
        .click();
    }

    self.setAuthor = function(author) {
      var info = [author.author_type];
      
      if (author.gender) info.push(author.gender);
      if (author.race) info.push(author.race);

      $('.author-details', self.$authorWidget).removeClass('hidden').text(info.join(', '));
      $('.new-author-details', self.$authorWidget).addClass('hidden');
    };

    self.setNewAuthor = function() {
      // TODO: show the new author form widgets,
      // include type of author, race, gender
      $('.author-details', self.$authorWidget).addClass('hidden');
      $('.new-author-details', self.$authorWidget).removeClass('hidden');
    };
  };
})(jQuery, window);

$(function() {
  Dexter.documentView = new Dexter.DocumentView().init();
  new Dexter.EditDocumentView().init();
});
Dropzone.autoDiscover = false;
