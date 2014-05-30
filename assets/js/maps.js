(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  Dexter.Maps = function() {
    var self = this;

    self.init = function() {
      if ($('#slippy-map').length === 0) {
        return;
      }

      self.map = L.map('slippy-map');
      self.map.setView({lat: -28.4796, lng: 24.698445}, 5);

      var osm = new L.TileLayer('//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom: 5,
        maxZoom: 12,
        attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'});
      self.map.addLayer(osm);
    };

    self.invalidate = function() {
      self.map.invalidateSize(false);
    };

    self.placesUrl = function() {
      var url = document.location;

      if (document.location.search === "") {
        url = url + "?";
      } else {
        url = url + "&";
      }

      return url + "format=places-json";
    };

    self.loadAndDrawPlaces = function() {
      $.getJSON(self.placesUrl(), self.drawPlaces);
    };

    self.drawPlaceMarker = function(place, coords, radius) {
      L.circleMarker(coords, {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5
      })
        .setRadius(radius)
        .addTo(self.map)
        .bindPopup(place.full_name + " (" + place.documents.length + ")");
    };

    self.drawPlaces = function(data) {
      var total = data.document_count;

      _.each(data.mentions, function(place) {
        // radius is between 5 and 25, based on the %age of all documents
        // this place relates to
        var radius = 5 + 30 * (place.documents.length / total);

        if (place.type == 'point') {
          // it's a point
          self.drawPlaceMarker(place, place.coordinates, radius);
        } else {
          // it's a region, get the centroid
          d3.json("https://maps.code4sa.org/political/2011/" + place.level + '?filter[' + place.level + ']=' + place.code + '&quantization=5000', function(error, topo) {
            if (!topo)
              return;

            var region = topojson.feature(topo, topo.objects.demarcation);
            var coords = d3.geo.centroid(region);
            self.drawPlaceMarker(place, [coords[1], coords[0]], radius);
          });
        }
      });
    };

    self.drawProvinces = function(click_callback){
      // add province boundaries
      $.getJSON("http://maps.code4sa.org/political/2011/province?quantization=1000", function (topo) {
        if (!topo)
          return;
        var featureLayer = L.geoJson(topojson.feature(topo, topo.objects.demarcation), {
          style: {
            "clickable": true,
            "color": "#00d",
            "fillColor": "#ccc",
            "weight": 1.0,
            "opacity": 0.3,
            "fillOpacity": 0.3,
          },
          onEachFeature: function (feature, layer) {
            var name = feature.properties['province_name'];
            var code = feature.properties['province'];

            layer.on('mouseover', function () {
              layer.setStyle({
                "fillOpacity": 0.5,
                "weight": 2.0,
                "opacity": 0.5,
              });
            });
            layer.on('mouseout', function () {
              layer.setStyle({
                "fillOpacity": 0.3,
                "weight": 1.0,
                "opacity": 0.3,
              });
            });
            layer.on('click', function () {
              click_callback(feature.id);
            });
          },
        });
        if(!self.map.provinceLayer)
          self.map.fitBounds(featureLayer);
        self.map.provinceLayer = featureLayer;
        self.map.addLayer(self.map.provinceLayer);
      });
    }

    self.drawMunicipalities = function(province_id, click_callback){
      if(self.map.municipalityLayer)
        self.map.removeLayer(self.map.municipalityLayer);
      // add municipality boundaries
      $.getJSON("http://maps.code4sa.org/political/2011/municipality?quantization=1000&filter[province]=" + province_id, function (topo) {
        if (!topo)
          return;
        var featureLayer = L.geoJson(topojson.feature(topo, topo.objects.demarcation), {
          style: {
            "clickable": true,
            "color": "#00d",
            "fillColor": "#ccc",
            "weight": 1.0,
            "opacity": 0.3,
            "fillOpacity": 0.3,
          },
          onEachFeature: function (feature, layer) {
            var name = feature.properties['municipality_name'];
            var code = feature.properties['municipality'];

            layer.on('mouseover', function () {
              layer.setStyle({
                "fillOpacity": 0.5,
                "weight": 2.0,
                "opacity": 0.5,
              });
            });
            layer.on('mouseout', function () {
              layer.setStyle({
                "fillOpacity": 0.3,
                "weight": 1.0,
                "opacity": 0.3,
              });
            });
            layer.on('click', function () {
              // it's a region, get the centroid
              var coords = d3.geo.centroid(feature.geometry);
              // center map around centroid
              self.map.panTo({lat: coords[1], lng: coords[0]});
              click_callback(feature.id);
            });
          },
        });
        self.map.fitBounds(featureLayer);
        self.map.municipalityLayer = featureLayer;
        self.map.addLayer(self.map.municipalityLayer);
      });
    }
  };
})(jQuery, window);

$(function() {
  Dexter.maps = new Dexter.Maps();
  Dexter.maps.init();
});
