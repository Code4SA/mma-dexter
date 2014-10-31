(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document activity pages
  Dexter.ActivityView = function() {
    var self = this;

    self.init = function() {
      self.$form = $('form.activity-refine');
      self.$form.find('.btn.download').on('click', self.download);
      self.$form.find('.remove-cluster').on('click', self.removeCluster);
    };

    self.removeCluster = function(e) {
      e.preventDefault();

      self.$form.find('input[name=cluster_id]').val('');
      self.$form.find('.analysis_nature').removeClass('hidden');
      self.$form.find('.cluster').remove();
    };

    self.download = function(e) {
      e.preventDefault();

      var old_action = self.$form.attr('action');

      self.$form.append('<input type="hidden" name="format" value="xlsx">');
      self.$form.attr('action', '/activity');
      self.$form.submit();

      self.$form.attr('action', old_action);
      $('input[name="format"]', self.$form).remove();
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
