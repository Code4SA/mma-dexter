$(function() {
  /**
   * Create a constructor for sparklines that takes some sensible defaults and merges in the individual
   * chart options. This function is also available from the jQuery plugin as $(element).highcharts('SparkLine').
   */
  Highcharts.SparkLine = function (options, callback) {
    var defaultOptions = {
      series: {
        pointStart: 1
      },
      chart: {
        renderTo: (options.chart && options.chart.renderTo) || this,
        backgroundColor: null,
        borderWidth: 0,
        type: 'area',
        margin: [2, 0, 2, 0],
        width: 120,
        height: 20,
        style: {
          overflow: 'visible'
        },
        skipClone: true
      },
      title: {
        text: ''
      },
      credits: {
        enabled: false
      },
      xAxis: {
        labels: {
          enabled: false
        },
        title: {
          text: null
        },
        startOnTick: false,
        endOnTick: false,
        tickPositions: []
      },
      yAxis: {
        endOnTick: false,
        startOnTick: false,
        labels: {
          enabled: false
        },
        title: {
          text: null
        },
        tickPositions: [0]
      },
      legend: {
        enabled: false
      },
      tooltip: {
        backgroundColor: null,
        borderWidth: 0,
        shadow: false,
        useHTML: true,
        hideDelay: 0,
        shared: true,
        padding: 0,
        positioner: function (w, h, point) {
          return { x: point.plotX - w / 2, y: point.plotY - h};
        },
        headerFormat: '',
        pointFormat: '{point.y}'
      },
      plotOptions: {
        series: {
          animation: false,
          lineWidth: 2,
          shadow: false,
          states: {
            hover: {
              lineWidth: 2
            }
          },
          marker: {
            radius: 0,
            states: {
              hover: {
                radius: 2
              }
            }
          },
          fillOpacity: 0.25
        },
        column: {
          negativeColor: '#910000',
          borderColor: 'silver'
        }
      }
    };
    options = Highcharts.merge(defaultOptions, options);

    return new Highcharts.Chart(options, callback);
  };

  $.fn.sparkline = function(options) {
    this.each(function(i, e) {
      var $e = $(e);

      var opts = {
        series: [{
          data: $.map($e.data('sparkline').split(','), parseFloat),
        }]
      };

      if ($e.data('label')) {
        opts.tooltip = {pointFormat: $e.data('label')};
      }

      opts = Highcharts.merge(opts, options);

      $e.highcharts('SparkLine', opts);
    });
  };

  $('*[data-sparkline]').sparkline();
});
