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

    self.datePairs = function(data) {
      // transform {"YYYY/MM/DD": 10} into [msecs, 10], sorted by date
      return _.map(_.keys(data).sort(), function(key) {
        return [moment(key, 'YYYY/MM/DD').valueOf(), data[key]];
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

    self.drawCharts = function(charts) {
      // time of creation
      var data = charts.charts.created.values;
      self.fillDates(data);
      $('.chart-created').highcharts({
        chart: {type: 'line'},
        xAxis: {type: 'datetime'},
        series: [{data: self.datePairs(data) }],
      });

      // time of publication
      data = charts.charts.published.values;
      cats = _.keys(data);
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-published').highcharts({
        chart: {type: 'column'},
        xAxis: {type: 'datetime'},
        series: [{data: self.datePairs(data)}],
      });

      // user
      data = charts.charts.users.values;
      cats = _.sortBy(_.keys(data), function(k) { return -data[k]; });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-users').highcharts({
        chart: {type: 'bar'},
        xAxis: {
          categories: cats,
          labels: {step: 1},
        },
        series: [{data: vals}],
      });

      // media
      data = charts.charts.media.values;
      types = charts.charts.media.types;

      // sort by media type, then by data values
      cats = _.keys(data).sort(function(a, b) {
        if (types[a] == types[b]) {
          return data[b] - data[a];
        } else {
          return types[a] < types[b] ? -1 : 1;
        }
      });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-media').highcharts({
        chart: {type: 'bar'},
        xAxis: {
          categories: cats,
          labels: {
            step: 1,
            formatter: function(v) {
              if (this.value.length > 15) {
                return this.value.slice(0, 15) + "...";
              } else {
                return this.value;
              }
            }
          }
        },
        series: [{data: vals}],
      });

      // fairness
      data = charts.charts.fairness.values;
      // don't plot Fair documents, it dominates too much
      delete data.Fair;
      cats = _.sortBy(_.keys(data), function(k) { return -data[k]; });
      vals = _.map(cats, function(k) { return data[k]; });
      $('.chart-fairness').highcharts({
        chart: {type: 'column'},
        xAxis: {categories: cats},
        series: [{data: vals}],
      });

      // problems
      data = charts.charts.problems.values;
      var holder = $('.chart-problems');
      if (data.length > 0) {
        holder.empty();
        _.map(data, function(val, cat) {
          holder.append('<div class="problem"><h3>' + val + '</h3><h4>' + cat + '</div>');
        });
      } else {
        holder.html('None');
      }
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
