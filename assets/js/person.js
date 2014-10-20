(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when editing person details
  Dexter.ShowPersonView = function() {
    var self = this;

    self.init = function() {
      if ($('#show-person').length === 0) {
        return;
      }

      self.personId = $('#show-person').data('person-id');
      self.personName = $('#show-person').data('person-name');

      $('.gender-race a.edit').on('click', function(e) {
        e.preventDefault();
        $('.gender-race').hide();
        $('.gender-race-controls').show();
      });

      $('.gender-race-controls a.cancel').on('click', function(e) {
        e.preventDefault();
        $(this).closest('form')[0].reset();

        $('.gender-race').show();
        $('.gender-race-controls').hide();
      });

      $('.aliases a.edit').on('click', function(e) {
        e.preventDefault();
        $('.aliases').hide();
        $('.aliases-controls').show();
      });

      $('.aliases-controls a.cancel').on('click', function(e) {
        e.preventDefault();
        $(this).closest('form')[0].reset();

        $('.alias-list .new').remove();
        $('.aliases').show();
        $('.aliases-controls').hide();
      });

      // person entity name autocomplete
      self.entityHound = new Bloodhound({
        name: 'people',
        remote: {
          url: '/api/entities?limit=5&q=%QUERY',
          filter: function(resp) { return resp.entities; },
        },
        dupDetector: function(remote, local) { return remote.id == local.id; },
        datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name); },
        queryTokenizer: Bloodhound.tokenizers.whitespace
      });
      self.entityHound.initialize();

      $('.new-alias-name').typeahead({
        highlight: true,
        autoselect: true,
      }, {
        source: self.entityHound.ttAdapter(),
        displayKey: self.entityName,
      }).on('typeahead:selected', function(e, entity, dataset) {
        self.newAlias(entity);
        $('.new-alias-name').typeahead('val', '');
      });

      // setup merging dialog
      self.lastMergeSearch = "";
      $('#merge-modal')
        .on('keyup', 'input[name="search"]', self.refreshMergeSearch)
        .on('show.bs.modal', self.updateMergeSearch);
    };

    // refresh the merge search item results on a keypress
    self.refreshMergeSearch = function(e) {
      if (self.mergeSearchTimeout) window.clearTimeout(self.mergeSearchTimeout);
      if ($(this).val() == self.lastMergeSearch) return;

      self.mergeSearchTimeout = window.setTimeout(self.updateMergeSearch, 300);
    };

    self.updateMergeSearch = function() {
      var text = $('#merge-modal input[name="search"]').val(),
          params = {};

      if (text.trim() === "") {
        text = self.personName;
        params.similar = '1';
      }

      params.q = text;
      self.lastMergeSearch = text;

      $.getJSON('/api/people', params, function(data) {
        var holder = $('#merge-modal ul.suggestions').empty();

        $.each(data.people.slice(0, 50), function(i, p) {
          if (p.id != self.personId) {
            holder.append('<li><a data-method="post" data-confirm="Are you sure?" href="/people/' + p.id + '/merge?mergein=' + self.personId + '">' + p.name);
          }
        });
      });
    };

    self.newAlias = function(entity) {
      var $new = $('ul.alias-list li:eq(0)').clone().addClass('new');

      $('input', $new).
        attr('id', 'alias_entity_ids-' + entity.id).
        attr('value', entity.id);

      $('label', $new).
        attr('for', 'alias_entity_ids-' + entity.id).
        text(self.entityName(entity));

      $('.alias-list').append($new);
    };

    self.entityName = function(e) {
      return e.name + ' (' + e.group + ', ' + e.id + ')';
    };

  };
})(jQuery, window);

$(function() {
  new Dexter.ShowPersonView().init();
});
