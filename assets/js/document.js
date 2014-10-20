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
        .on('click', '.attachment', self.showAttachment);

      // setup the offset adjustments for hilighting portions of the article
      self.$articleText = $('.document-container .article-text');
      self.originalText = self.$articleText.data('original') || '';

      $('.document-container .tabs a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
        // highlight entities for the active pane
        self.highlightEntities($($(e.target).attr('href')));
      });

      $('.document-container .offsets [data-offsets]').on('mouseover', function(e) {
        self.highlightEntities($(this));
      });

      $('.document-container .offsets [data-offsets]').on('mouseout', function(e) {
        self.highlightEntities($('.document-container .tab-pane.active'));
      });

      self.highlightEntities($('.document-container .tab-pane.active'));

      return self;
    };

    self.highlightOffsets = function(offsets) {
      var text = self.originalText;
      var accumulatedOffset = 0;

      for (var i = 0; i < offsets.length; i++) {
        var offset = offsets[i];
        offset[0] += i * 13;

        text = text.slice(0, offset[0]) +
          '<mark>' + text.slice(offset[0], offset[0]+offset[1]) + '</mark>' +
          text.slice(offset[0]+offset[1]);
      }

      // Do HTML escape and unescape the mark tags. This technically lets
      // someone inject mark tags, but we're okay with that, it makes this easy.
      text = self.htmlEscape(text)
        .replace(/\&lt;mark\&gt;/g, '<mark>')
        .replace(/\&lt;\/mark&gt;/g, '</mark>')
        // now add <br> in the same way the server does
        .replace(/\n+/g, "\n")
        .replace(/\n/g, "\n")
        .replace(/\n/g, "</p>");

      self.$articleText.html('<p>' + text + '</p>');
    };

    self.highlightEntities = function(container) {
      var $elems;

      if ($(container).data('offsets')) {
        $elems = $(container);
      } else {
        $elems = $('[data-offsets]', $(container));
      }

      var offsets = $.makeArray($elems.map(function(i, row) { return $(row).data('offsets'); }));
      if (offsets.length > 0) {
        offsets = offsets.join(' ').trim().split(/ +/);
        offsets = $.map(offsets, function(e) {
          var pair = e.split(':');
          return [[parseInt(pair[0]), parseInt(pair[1])]];
        });

        offsets.sort(function(a, b) { return a[0] - b[0]; });

        // coalesce overlapping offsets
        var coalesced = [offsets[0]];

        for (var i = 1; i < offsets.length; i++) {
          var prev = coalesced[coalesced.length-1];
          var curr = offsets[i];

          if (curr[0] <= prev[0] + prev[1]) {
            prev[1] = Math.max(prev[0] + prev[1], curr[0] + curr[1]) - prev[0];
          } else {
            coalesced.push(curr);
          }
        }

        offsets = coalesced;
      }

      self.highlightOffsets(offsets);
    };

    self.htmlEscape = function(str) {
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/"/g, '&quot;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;');
    };

    self.showArticleText = function(e) {
      e.preventDefault();
      $('.article-content .article-text').show();
      $('.attachment-viewer').hide();
    };

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

      self.$form = $('form.edit-document, form.new-document');

      $('button.submit').on('click', function(e) {
        self.$form.submit();
      });

      $('#country_id')
        .on('change', self.countryChanged)
        .trigger('change');

      // author name autocomplete
      self.$authorName = $('#author-name');
      self.$authorWidget = $('.author-widget');

      self.authorHound = new Bloodhound({
        name: 'authors',
        remote: {
          url: '/api/authors?limit=5&q=%QUERY',
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
          dictDefaultMessage: "Click or drag-and-drop to add an attachment",
        });
      self.dropzone
        .on('success', self.attachmentUploaded)
        .on('addedfile', function(e) { $('#dropzone .dz-preview:last-child').append('<i class="fa fa-spinner fa-spin fa-4x">'); });

      // show the first attachment, if any
      $('.attachment-list li:not(.template) .attachment').first().click();

      // attachment viewer
      $('.attachment-list')
        .on('click', '.delete', self.deleteAttachment);

      self.$form[0].dirty = false;
    };

    self.attachmentUploaded = function(file) {
      // successfully uploaded
      self.dropzone.removeFile(file);

      // the form is now dirty
      self.$form[0].dirty = true;

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
    };

    self.deleteAttachment = function(e) {
      e.preventDefault();

      // the form is now dirty
      self.$form[0].dirty = true;

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

    self.countryChanged = function(e) {
      // change the list of mediums to show only those for this country

      // build up a list of mediums by country if we don't already have one
      if (!self.mediums) {
        self.mediums = {}
        $('#medium_id optgroup option').each(function(i, opt) {
          var country = $(opt).parent().attr('label');
          if (!self.mediums[country])
            self.mediums[country] = [];
          self.mediums[country].push({value: opt.value, text: opt.textContent});
        });
      }

      var $medium = $('#medium_id'),
          selected = $medium.val(),
          selectedValid = false;

      $medium
        .select2('destroy')
        .empty()
        .append($("<option value=''>(none)</option>"));

      var country = $('option:selected', this).text();
      $.each(self.mediums[country], function(i, opt) {
        selectedValid = selectedValid || (opt.value == selected);

        $("<option>")
          .attr('value', opt.value)
          .text(opt.text)
          .appendTo($medium);
      });

      $medium
        .val(selectedValid ? selected : '')
        .select2();
    };
  };
})(jQuery, window);

$(function() {
  Dexter.documentView = new Dexter.DocumentView().init();
  new Dexter.EditDocumentView().init();
});
Dropzone.autoDiscover = false;
