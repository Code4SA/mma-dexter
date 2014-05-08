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

      self.drawFeatures();
    };

    self.drawFeatures = function() {
      $('.geo-feature').each(function(i, feat) {
        console.log(feat);

        var $feat = $(feat);
        var geo = $feat.data('geo-data');
        var parts;

        if ($feat.data('geo-type') == 'point') {
          parts = geo.split(',');
          var lat = parseFloat(parts[0]),
              lng = parseFloat(parts[1]);

          L.marker([lat, lng])
            .addTo(self.map)
            .bindPopup($('td:first-child', $feat).text());

        } else {
          parts = geo.split('-');
          var level = parts[0],
              code = parts[1];

          d3.json("http://maps.code4sa.org/political/2011/" + level + '?filter[' + level + ']=' + code + '&quantization=5000', function(error, topo) {
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
