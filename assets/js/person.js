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
      self.personHound = new Bloodhound({
        name: 'people',
        prefetch: {
          url: '/api/entities/person',
          ttl: 3600*1000,
          filter: function(resp) { return resp.entities; },
        },
        remote: {
          url: '/api/entities?q=%QUERY',
          filter: function(resp) { return resp.entities; },
        },
        sorter: function(a, b) {
          // compare on length, then alphabetically
          if (a.name.length == b.name.length) {
            return a.name.localeCompare(b.name);
          } else {
            return a.name.length - b.name.length;
          }
        },
        dupDetector: function(remote, local) { return remote.id == local.id; },
        datumTokenizer: function(d) { return Bloodhound.tokenizers.whitespace(d.name); },
        queryTokenizer: Bloodhound.tokenizers.whitespace
      });
      self.personHound.initialize();

      $('.new-alias-name').typeahead({
        highlight: true,
        autoselect: true,
      }, {
        source: self.personHound.ttAdapter(),
        displayKey: self.entityName,
      }).on('typeahead:selected', function(e, entity, dataset) {
        self.newAlias(entity);
        $('.new-alias-name').typeahead('val', '');
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
