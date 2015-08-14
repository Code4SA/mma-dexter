(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view to help the user do mass operations on selected
  // documents in the activity view
  Dexter.SelectionView = function() {
    var self = this;

    self.init = function() {
      self.all_doc_ids = $('#doc_ids').val().split(',');
      self.selected = [];
      self.$boxes = $('.activity-list input[type="checkbox"]');
      self.$boxes.on('click', self.updateSelection);
      self.$tools = $('.with-selection-tools');
      self.$tools.hide();

      $('.select-page').on('click', self.selectPage);
      $('.select-all').on('click', self.selectAll);
      $('.select-none').on('click', self.selectNone);
      $('.selected-add-tag').on('click', self.addTag);
      $('.selected-remove-tag').on('click', self.removeTag);
    };

    self.updateSelection = function() {
      if (self.all) {
        self.selected = self.all_doc_ids;
      } else {
        self.selected = self.$boxes.filter(':checked').map(function() {
          return this.value;
        }).toArray();
      }

      self.$tools.toggle(self.selected.length > 0);
      self.$tools.find('.count').text(self.selected.length);
    };

    self.selectPage = function(e) {
      e.preventDefault();
      self.$boxes.prop('checked', true);
      self.all = false;
      self.updateSelection();
    };

    self.selectAll = function(e) {
      self.selectPage(e);
      self.all = true;
      self.updateSelection();
    };

    self.selectNone = function(e) {
      e.preventDefault();
      self.$boxes.prop('checked', false);
      self.all = false;
      self.updateSelection();
    };

    self.addTag = function(e) {
      e.preventDefault();

      var tag = prompt('What tags do you want to add?');
      tag = (tag || '').trim();

      if (tag) {
        $.post('/articles/add-tag', {
          tag: tag,
          doc_ids: self.selected.join(','),
        })
        .then(function() {
          window.location.reload(true);
        });
      }
    };

    self.removeTag = function(e) {
      e.preventDefault();

      var tag = prompt('What tags do you want to remove?');
      tag = (tag || '').trim();

      if (tag) {
        $.post('/articles/remove-tag', {
          tag: tag,
          doc_ids: self.selected.join(','),
        })
        .then(function() {
          window.location.reload(true);
        });
      }
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.SelectionView().init();
});
