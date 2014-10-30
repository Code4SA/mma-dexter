(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at the dashboard topics pages
  Dexter.DashboardTopicsView = function() {
    var self = this;

    self.init = function() {
      self.key = 'size';
      self.dirn = 1;

      $('.sort-buttons input').on('change', self.sortButtonClick);
    };

    self.sortButtonClick = function(e) {
      self.key = $(this).val();

      if (self.key[0] == "-") {
        self.dirn = -1;
        self.key = self.key.slice(1);
      } else {
        self.dirn = 1;
      }

      self.sortTopics();
    };

    self.sortTopics = function() {
      var $topicList = $('.topic-list'),
          $topics = $topicList.find('.topic');

      $topics.remove().sort(function(a, b) {
        return self.dirn * (+$(a).data(self.key) - +$(b).data(self.key));
      }).appendTo($topicList);
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.DashboardTopicsView().init();
});
