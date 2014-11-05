(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document sources activity pages
  Dexter.ActivitySourcesView = function() {
    var self = this;

    self.init = function() {
      $('a.show-utterances').on('click', self.toggleUtterances);
    };

    self.toggleUtterances = function(e) {
      e.preventDefault();
      $(this).parent().parent().next('.utterances').toggleClass('hidden');
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivitySourcesView().init();
});
