(function($, exports) {
  if (typeof exports.Dexter == 'undefined') exports.Dexter = {};
  var Dexter = exports.Dexter;

  // view when looking at all document activity pages
  Dexter.ActivityView = function() {
    var self = this;

    self.init = function() {
      self.$form = $('form.activity-refine');
      self.$form.find('input[type=submit]').on('click', self.submitForm);
      self.$form.find('.download').on('click', self.download);
      self.$form.find('.remove-cluster').on('click', self.removeCluster);
      self.$form.find('.analysis_nature a').on('click', self.setAnalysisNature);

      // setup person search form
      self.$form.find("*[name=source_person_id]").select2({
        placeholder: "Find a person...",
        minimumInputLength: 2,
        containerCssClass: 'form-control',
        allowClear: true,
        ajax: { // instead of writing the function to execute the request we use Select2's convenient helper
          url: "/api/people",
          dataType: 'json',
          quietMillis: 250,
          cache: true,
          data: function (term, page) {
            return {q: term};
          },
          results: function (data, page) {
            var people = $.map(data.people, function(p) {
              return {id: p.id, text: p.name};
            });
            return {results: people};
          }
        },
        initSelection: function(element, callback) {
          var text = element.data('text'),
              id = element.val(),
              data = null;

          if (id && text) {
            data = {id: id, text: text};
          }

          callback(data);
        }
      });
    };

    self.setAnalysisNature = function(e) {
      var nature = $(this).data('nature');
      var $elem = $(this);

      self.$form.find('[name=analysis_nature_id]').val(nature);
      self.$form.find('.analysis_nature i.fa-check').remove();
      self.$form.find('.analysis_nature li.disabled').toggleClass('disabled');
      self.$form.find('.analysis_nature button.dropdown-toggle').html($elem.html() + '<span class="caret"></span>');

      $elem
        .prepend('<i class="fa fa-check"></i>')
        .parent('li')
        .addClass('disabled');
    },

    self.removeCluster = function(e) {
      e.preventDefault();

      self.$form.find('input[name=cluster_id]').val('');
      self.$form.find('.analysis_nature').removeClass('hidden');
      self.$form.find('.cluster').remove();
    };

    self.submitForm = function(e) {
      $(this)
        .prop('disabled', true)
        .val('Working...');

      self.$form.submit();
    };

    self.download = function(e) {
      e.preventDefault();

      var old_action = self.$form.attr('action');

      self.$form.find('input[name=format]').val($(this).data('format'));
      self.$form.attr('action', '/activity');
      self.$form.submit();

      self.$form.attr('action', old_action);
      self.$form.find('input[name=format]').val('');
    };
  };
})(jQuery, window);

$(function() {
  new Dexter.ActivityView().init();
});
