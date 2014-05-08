(function($, exports) {
  Dexter.Maps = function() {
    var self = this;

    self.init = function() {
      if ($('#slippy-map').length === 0) {
        return;
      }

      // resize maps when a tab is toggled
      $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
        $($(this).attr('href') + ' .leaflet-container').each(function(i, map) {
          self.map.invalidateSize(false);
        });
      });

      self.map = L.map('slippy-map');
      self.map.setView({lat: -28.4796, lng: 24.698445}, 5);

      var osm = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        minZoom: 1,
        maxZoom: 16,
        attribution: 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'});	
      self.map.addLayer(osm);

      self.loadAndDrawPlaces();
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

    self.drawPlaces = function(data) {
      _.each(data.mentions, function(place) {
        if (place.type == 'point') {
          // it's a point
          L.marker(place.coordinates)
            .addTo(self.map)
            .bindPopup(place.full_name + " (" + place.documents.length + ")");

        } else {
          // it's a region
          d3.json("http://maps.code4sa.org/political/2011/" + place.level + '?filter[' + place.level + ']=' + place.code + '&quantization=5000', function(error, topo) {
            if (!topo)
              return;

            var featureLayer = L.geoJson(topojson.feature(topo, topo.objects.demarcation), {
              style: {
                "clickable": false,
                "color": "#00d",
                "fillColor": "#ccc",
                "weight": 1.0,
                "opacity": 0.5,
                "fillOpacity": 0.5,
              },
            });
            self.map.addLayer(featureLayer);
          });
        }
      });
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.Maps().init();
});
