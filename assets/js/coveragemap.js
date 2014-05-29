(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at media coverage
  Dexter.CoverageView = function() {
    var self = this;

    self.placesSetup = false;

    self.init = function() {
      $('form.activity-refine .btn.download').on('click', function(e) {
        e.preventDefault();

        $('form.activity-refine').append('<input type="hidden" name="format" value="xlsx">');
        $('form.activity-refine').submit();
        $('form.activity-refine input[name="format"]').remove();
      });

      // invalidate the map so that it gets resized correctly
      $($(this).attr('href') + ' .leaflet-container').each(function(i, map) {
        Dexter.maps.invalidate();
      });

      if (!self.placesSetup) {
        Dexter.maps.loadAndDrawPlaces();
        self.placesSetup = true;
        Dexter.maps.drawProvinces();
      }
    };

    self.datePairs = function(data) {
      // transform {"YYYY/MM/DD": 10} into [msecs, 10], sorted by date
      return _.map(_.keys(data).sort(), function(key) {
        return [moment.utc(key, 'YYYY/MM/DD').valueOf(), data[key]];
      });
    };

    self.fillDates = function(data) {
      // ensure that we have datapoints for all dates in this range
      var keys = _.keys(data).sort();
      var min = moment(keys[0], 'YYYY-MM-DD'),
          max = moment(keys[keys.length-1], 'YYYY-MM-DD');

      for (var d = min.clone(); !d.isAfter(max); d.add(1, 'days')) {
        var s = d.format('YYYY/MM/DD');
        if (!(s in data)) {
          data[s] = 0;
        }
      }
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.CoverageView().init();
});
