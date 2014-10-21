(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document sources activity pages
  Dexter.ActivitySourcesView = function() {
    var self = this;

    self.init = function() {
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivitySourcesView().init();
});
