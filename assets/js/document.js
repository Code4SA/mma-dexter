(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when editing document details (NOT the analysis)
  Dexter.EditDocumentView = function() {
    var self = this;

    self.init = function() {
      if ($('#new-document, #edit-document').length === 0) {
        return;
      }

      // author name autocomplete
      self.$authorWidget = $('.author-widget');
      self.authorHound = new Bloodhound({
        name: 'authors',
        prefetch: {
          url: '/api/authors',
          ttl: 600,
          filter: function(resp) { return resp.authors; },
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
      self.$authorName = $('#author-name');

      self.$authorName.typeahead({
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
  };

  // view when editing the document analysis
  Dexter.EditDocumentAnalysisView = function() {
    var self = this;

    self.init = function() {
      self.$form = $('form.edit-analysis');
      if (self.$form.length === 0) {
        return;
      }

      // source person name autocomplete
      self.personHound = new Bloodhound({
        name: 'people',
        prefetch: {
          url: '/api/people',
          ttl: 600,
          filter: function(resp) { return resp.people; },
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
      self.personHound.initialize();

      self.newSourceCount = $('.sources tr.new', self.$form).length;

      $('.btn.add-source').on('click', self.addSource);
      $('table.sources', self.$form).
        on('click', '.btn.delete', self.deleteSource).
        on('click', '.btn.undo-delete', self.undoDeleteSource).
        on('change', 'input:radio[name$="-source_type"]', self.toggleSourceType);

      self.newFairnessCount = $('.fairness tr.new', self.$form).length;
      $('table.fairness', self.$form).
        on('change', '.template select', self.addNewFairness).
        on('click', '.btn.delete', self.deleteFairness).
        on('click', '.btn.undo-delete', self.undoDeleteFairness);
    };
      
    self.addSource = function(e) {
      e.preventDefault();

      var $template = $('table.sources tr.template');
      var $row = $template.clone().insertBefore($template);

      // this row is no longer a template
      $row.removeClass('template').addClass('new');

      self.newSourceCount++;

      // change form field name and 'for' prefixes to be new[ix]
      $('input, select, textarea, label', $row).each(function() {
        var attrs = ['name', 'id', 'for'];

        for (var i = 0; i < attrs.length; i++) {
          var attr = attrs[i];
          var val = $(this).attr(attr);
          if (val) {
            $(this).attr(attr, val.replace('new-', 'new[' + self.newSourceCount + ']-'));
          }
        }
      });

      $('.chosen-select-delayed', $row).chosen();

      self.personTypeaheadEnabled = false;
      self.enablePersonTypeahead($row);
    };

    self.enablePersonTypeahead = function($row) {
      if (!self.personTypeaheadEnabled) {
        $('.person-name input', $row).
          val('').
          typeahead({
            highlight: true,
            autoselect: true,
          }, {
            source: self.personHound.ttAdapter(),
            displayKey: 'name',
          }).
          on('typeahead:selected', self.personSourceChosen);

        self.personTypeaheadEnabled = true;
      }
    };

    self.disablePersonTypeahead = function($row) {
      $('.person-name input', $row).typeahead('destroy').val('');
      self.personTypeaheadEnabled = false;
    };

    // a new person was chosen as a source from the typeahead box
    self.personSourceChosen = function(event, person, datasource) {
      var $row = $(this).closest('tr');
      var $select = $('select[name$="affiliation_id"]', $row);

      // find the matching affiliation option
      var affiliationId = $('option', $select).
        filter(function(i, opt) { return opt.innerText == person.affiliation; }).
        first().
        attr('value') || '';

      // choose the affiliation
      $select.
        val(affiliationId).
        trigger('chosen:updated');

      // clear the source function
      $('select[name$="source_function_id"]', $row).val('');
    };

    // delete button was clicked
    self.deleteSource = function(e) {
      e.preventDefault();

      var $row = $(this).closest('tr');
      if ($row.hasClass('new')) {
        // it's new
        $row.remove();
      } else {
        // it's not new
        $row.addClass('deleted');
        $('input[name$="-deleted"]', $row).val('1');
      }
    };

    // undo a source delete
    self.undoDeleteSource = function(e) {
      e.preventDefault();

      var $row = $(this).closest('tr');
      $row.removeClass('deleted');
      $('input[name$="-deleted"]', $row).val('0');
    };

    // should we show the unnamed-details area?
    self.toggleSourceType = function(e) {
      var $row = $(this).closest('tr');
      var sourceType = $(this).val();

      if (sourceType == 'unnamed') {
        $('.person-name', $row).hide();
        $('.unnamed-details', $row).show();

      } else {
        $('.person-name', $row).show();
        $('.unnamed-details', $row).hide();

        if (sourceType == 'person') {
          self.enablePersonTypeahead($row);
        } else {
          self.disablePersonTypeahead($row);
        }

        $('.person-name input', $row).focus();
      }
    };

    // when the user starts adding a new fairness, duplicate the row to keep a fresh
    // 'new entry' row, and then rename the elements on this one
    self.addNewFairness = function(e) {
      if ($(this).val() === '') return;

      var $row = $(this).closest('tr');
      var $template = $row.clone().insertAfter($row);
      $('select[type="text"]', $template).val('');

      // this row is no longer a template
      $row.removeClass('template').addClass('new');

      self.newFairnessCount++;

      // change form field name prefixes to be new[ix]
      $('select', $row).each(function() {
        $(this).attr('name', $(this).attr('name').replace('new-', 'new[' + self.newFairnessCount + ']-'));
      });

      // remove the (none) option
      $('select[name$="fairness_id"] > option', $row).each(function(i, opt) {
        if (opt.value === '') {
          $(opt).remove();
        }
      });

      $('.chosen-select-delayed', $row).chosen();
    };

    // delete button was clicked
    self.deleteFairness = function(e) {
      e.preventDefault();

      var $row = $(this).closest('tr');
      if ($row.hasClass('new')) {
        // it's new
        $row.remove();
      } else {
        // it's not new
        $row.addClass('deleted');
        $('select', $row).prop('disabled', true);
        $('input[name$="-deleted"]', $row).val('1');
      }
    };

    // undo a fairness delete
    self.undoDeleteFairness = function(e) {
      e.preventDefault();

      var $row = $(this).closest('tr');
      $row.removeClass('deleted');
      $('select', $row).prop('disabled', false);
      $('input[name$="-deleted"]', $row).val('0');
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.EditDocumentView().init();
  new Dexter.EditDocumentAnalysisView().init();
});
