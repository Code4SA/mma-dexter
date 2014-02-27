(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when editing person details
  Dexter.ShowPersonView = function() {
    var self = this;

    self.init = function() {
      if ($('#show-person').length === 0) {
        return;
      }

      $('.gender-race a.edit').on('click', function(e) {
        e.preventDefault();

        $('.gender-race').hide();
        $('form#edit-person').show();
      });

      $('form#edit-person a.cancel').on('click', function(e) {
        $('.gender-race').show();
        $('form#edit-person').hide();
      });

    };

    self.setAuthor = function(author) {
      var info = [author.author_type];
      
      if (author.gender) info.push(author.gender);
      if (author.race) info.push(author.race);

      $('.author-details', self.$authorWidget).removeClass('hidden').text(info.join(', '));
      $('.new-author-details', self.$authorWidget).addClass('hidden');
    };

    self.setNewAuthor = function() {
      // TODO: show the new author form widgets,
      // include type of author, race, gender
      $('.author-details', self.$authorWidget).addClass('hidden');
      $('.new-author-details', self.$authorWidget).removeClass('hidden');
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ShowPersonView().init();
});
