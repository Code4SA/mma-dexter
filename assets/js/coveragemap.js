(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at media coverage
  Dexter.CoverageView = function() {
    var self = this;

    // set global variables
    var form = $(".coverage-refine")
    var input_selected_province = form.find("input#selected_province")
    var input_selected_municipality = form.find("input#selected_municipality")
    var span_title = $("#map-area-title")

    var selected_province = input_selected_province.val()
    var selected_municipality = input_selected_municipality.val()

    if(selected_province)
      console.log(selected_province)
    else
      console.log("no province selected")
    if(selected_municipality)
      console.log(selected_municipality)
    else
      console.log("no municipality selected")

    //Width and height
    var w = 800;
    var h = 600;

    //Define map projection
    var projection = d3.geo.mercator()
      .translate([w/2, h/2])
      .center([25.48, -28.76])
      .scale([2000]);

    //Define path generator
    var path = d3.geo.path()
      .projection(projection);

    //Create SVG element
    var svg = d3.select("#coverage-map")
      .append("svg")
      .attr("width", w)
      .attr("height", h);

    self.init = function() {
      d3.json("https://maps.code4sa.org/political/2011/province?filter&quantization=5000", function(error, topo) {
        if (error){
          $("#slippy-map").text("No data available.")
          return
        }

        //Bind data and create one path per GeoJSON feature
        svg.selectAll("path")
          .data(topojson.feature(topo, topo.objects.demarcation).features)
          .enter()
          .append("path")
          .attr("class", function(d) { return "province " + d.id; })
          .attr("d", path);
      });

      self.load_and_draw_chart()
    };

    self.load_and_draw_chart = function(){
      // load chart data
      $.getJSON(self.placesUrl(), function(data){
        console.log(data)
        if(selected_province)
          data = data['provinces'][selected_province]
        if(selected_municipality)
          data = data['municipalities'][selected_municipality]
        if(data)
          self.drawChart(data);
        else
          $(".chart.chart-media-coverage").text("No data available.")
      });
    }

    self.placesUrl = function() {
      var url = document.location;

      if (document.location.search === "") {
        url = url + "?";
      } else {
        url = url + "&";
      }

      return url + "format=places-json";
    };

    self.drawChart = function(chart_data) {

      // charts
      var cats = []
      var vals = []
      var medium_breakdown = chart_data.medium_breakdown;

      for (var medium in medium_breakdown) {
        if (medium_breakdown.hasOwnProperty(medium)) {
          cats.push(medium);
          vals.push(medium_breakdown[medium]);
        }
      }

      $('.chart-media-coverage').highcharts({
        chart: {
          type: 'column'
        },
        title: {
          text: '',
          style: {
            display: 'none'
          }
        },
        subtitle: {
          text: '',
          style: {
            display: 'none'
          }
        },
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
        yAxis: {
          title: {
            text: 'number of stories'
          }
        },
        series: [{
          showInLegend: false,
          data: vals
        }],
      });
    }
  };

})(jQuery, window);

$(function() {
  var coverage_view = new Dexter.CoverageView
  coverage_view.init()
});
