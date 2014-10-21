(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document sources activity pages
  Dexter.ActivitySourcesView = function() {
    var self = this;

    self.init = function() {
      $('*[data-sparkline]').each(function(i, e) {
        var $e = $(e);

        $e.highcharts('SparkLine', {
          series: [{
            data: $.map($e.data('sparkline').split(','), parseFloat),
            pointStart: 1
          }]
        });
      });
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivitySourcesView().init();
});
