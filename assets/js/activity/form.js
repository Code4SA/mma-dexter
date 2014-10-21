(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document activity pages
  Dexter.ActivityView = function() {
    var self = this;

    self.init = function() {
      $('form.activity-refine .btn.download').on('click', function(e) {
        e.preventDefault();

        $('form.activity-refine').append('<input type="hidden" name="format" value="xlsx">');
        $('form.activity-refine').submit();
        $('form.activity-refine input[name="format"]').remove();
      });
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
