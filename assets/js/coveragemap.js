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
    var width = 750;
    var height = 600;
    var active = d3.select(null);

    var transition_duration = 300;

    //Define map projection
    var projection = d3.geo.mercator()
      .translate([width/2, height/2])
      .center([25.48, -28.76])
      .scale([2000]);

    //Define path generator
    var path = d3.geo.path()
      .projection(projection);

    //Create SVG element
    var svg = d3.select("#coverage-map")
      .append("svg")
      .attr("width", width)
      .attr("height", height);

    svg.append("rect")
      .attr("class", "background")
      .attr("width", width)
      .attr("height", height)
      .on("click", reset);

    var g = svg.append("g")
      .style("stroke-width", "1.5px");

    function clicked(d) {
      if (active.node() === this) return reset();
      var feature_id = d.id;
      var feature_name = null
      if(d.properties.hasOwnProperty('province_name'))
      {
        feature_name = d.properties.province_name;
        load_municipalities(feature_id)
      }
      else if(d.properties.hasOwnProperty('municipality_name'))
        feature_name = d.properties.municipality_name;

      var centroid = projection(d3.geo.centroid(d));
      console.log(feature_id)

      active.classed("active", false);
      active = d3.select(this).classed("active", true);

      var bounds = path.bounds(d),
        dx = bounds[1][0] - bounds[0][0],
        dy = bounds[1][1] - bounds[0][1],
        x = (bounds[0][0] + bounds[1][0]) / 2,
        y = (bounds[0][1] + bounds[1][1]) / 2,
        scale = .9 / Math.max(dx / width, dy / height),
        translate = [width / 2 - scale * x, height / 2 - scale * y];

      g.transition()
        .duration(transition_duration)
        .style("stroke-width", 1.5 / scale + "px")
        .attr("transform", "translate(" + translate + ")scale(" + scale + ")");
    }

    function reset() {
      active.classed("active", false);
      active = d3.select(null);

      g.transition()
        .duration(transition_duration)
        .style("stroke-width", "1.5px")
        .attr("transform", "");
    }

    function load_provinces(){
      d3.json("https://maps.code4sa.org/political/2011/province?filter&quantization=2000", function(error, topo) {
        if (error){
          $("#coverage-map").text("No data available.")
          return
        }

        //Bind data and create one path per GeoJSON feature
        g.selectAll("path.province")
          .data(topojson.feature(topo, topo.objects.demarcation).features)
          .enter()
          .append("path")
          .attr("class", function(d) { return "feature province " + d.id; })
          .attr("d", path)
          .on("click", clicked);

        g.append("path")
          .datum(topojson.mesh(topo, topo.objects.demarcation, function(a, b) { return a !== b; }))
          .attr("class", "mesh province")
          .attr("d", path);
      });
    }

    function load_municipalities(province_id){
      d3.json("https://maps.code4sa.org/political/2011/municipality?filter&quantization=1000&filter[province]=" + province_id, function(error, topo) {
        if (error){
          $("#coverage-map").text("No data available.")
          return
        }
        
        g.selectAll("path.municipality").remove()

        //Bind data and create one path per GeoJSON feature
        g.selectAll("path.municipality")
          .data(topojson.feature(topo, topo.objects.demarcation).features)
          .enter()
          .append("path")
          .attr("class", function(d) { return "feature municipality " + d.id; })
          .attr("d", path)
          .on("click", clicked);

        g.append("path")
          .datum(topojson.mesh(topo, topo.objects.demarcation, function(a, b) { return a !== b; }))
          .attr("class", "mesh municipality")
          .attr("d", path);
      });
    }

    self.init = function() {
      load_provinces()
      self.load_and_draw_chart()
    }

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
