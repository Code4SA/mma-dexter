(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document activity pages
  Dexter.ActivityView = function() {
    var self = this;

    self.init = function() {
      $('form.activity-refine .btn.download').on('click', function(e) {
        e.preventDefault();

        var $form = $('form.activity-refine');
        var old_action = $form.attr('action');

        $form.append('<input type="hidden" name="format" value="xlsx">');
        $form.attr('action', '/activity');
        $form.submit();

        $form.attr('action', old_action);
        $('input[name="format"]', $form).remove();
      });
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
