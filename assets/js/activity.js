(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at document activity
  Dexter.ActivityView = function() {
    var self = this;

    self.init = function() {
      Highcharts.setOptions({
        chart: {
          animation: false,
        },
        plotOptions: {
          series: {
            animation: false,
          },
          column: {
            tooltip: {
              pointFormat: '<span style="color:{series.color}">\u25CF</span> <b>{point.y}</b><br/>',
            }
          },
          line: {
            tooltip: {
              pointFormat: '<span style="color:{series.color}">\u25CF</span> <b>{point.y}</b><br/>',
            }
          },
          bar: {
            tooltip: {
              pointFormat: '<span style="color:{series.color}">\u25CF</span> <b>{point.y}</b><br/>',
            }
          },
        },
        title: {
          text: null,
        },
        yAxis: {
          title: {
            text: null,
          },
          floor: 0,
        },
        legend: {
          enabled: false
        }
      });
      self.updateCharts();
    };

    self.chartUrl = function() {
      // TODO: update based on form
      var url = document.location;

      if (document.location.search === "") {
        url = url + "?";
      } else {
        url = url + "&";
      }

      return url + "format=chart-json";
    };
    
    self.updateCharts = function() {
      $.getJSON(self.chartUrl(), self.drawCharts);
    };

    self.drawCharts = function(charts) {
      // time of creation
      var data = charts.charts.created.values;
      var cats = _.keys(data);
      var vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-created').highcharts({
        chart: {type: 'line'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });

      // time of publication
      data = charts.charts.published.values;
      cats = _.keys(data);
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-published').highcharts({
        chart: {type: 'column'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });

      // user
      data = charts.charts.users.values;
      cats = _.sortBy(_.keys(data), function(k) { return -data[k]; });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-users').highcharts({
        chart: {type: 'column'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });

      // media
      data = charts.charts.media.values;
      cats = _.sortBy(_.keys(data), function(k) { return -data[k]; });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-media').highcharts({
        chart: {type: 'bar'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });

      // problems
      data = charts.charts.problems.values;
      cats = _.sortBy(_.keys(data), function(k) { return -data[k]; });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-problems').highcharts({
        chart: {type: 'column'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });
    };

    self.values = function(data, cats) {
      return $.map(cats, function(i, key) {
        return data[key];
      });
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
