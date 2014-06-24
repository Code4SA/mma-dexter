$(function() {
  $('[title]').tooltip();
  $('.select2:visible').select2();

  $('.use-datepicker').datepicker({
    format: 'yyyy/mm/dd',
    todayHighlight: true,
    autoclose: true,
  });
});

$(function() {
  $('.use-datetimepicker').datetimepicker({
    icons: {
      time: "fa fa-clock-o",
      date: "fa fa-calendar",
      up: "fa fa-arrow-up",
      down: "fa fa-arrow-down"
    },
  });
});

$(function() {
  var now = moment();
  var yesterday = now.clone().subtract(moment.duration(1, 'days'));

  $('.use-daterangepicker').daterangepicker({
    format: 'YYYY/MM/DD',
    opens: 'left',
    maxDate: now.clone().add(moment.duration(1, 'days')),
    ranges: {
      'Today': [now, now],
      'Yesterday': [yesterday, yesterday],
      'Last 7 days': [now.clone().subtract(moment.duration(7, 'days')), now],
      'Last 14 days': [now.clone().subtract(moment.duration(14, 'days')), now],
      'Last 30 days': [now.clone().subtract(moment.duration(30, 'days')), now],
      'Last 90 days': [now.clone().subtract(moment.duration(90, 'days')), now]
    }
  });
});

$(function() {
  // show
  $('button[data-clear="input-group"]').on('click', function(e) {
    e.preventDefault();
    $('input', $(this).closest('.input-group')).val('');
  });
});

// globally prevent enter key from submitting forms
$(function() {
  $(document).on('keydown', 'input[type!="submit"], select', function(event) {
    if (!$(this).hasClass('allow-enter') && event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  });
});

$(function() {
  // prevent dirty forms from being navigated away from
  var dirty = false;

  $('form.safedirty').on('change', 'input, select, textarea', function(e) {
    e.delegateTarget.dirty = true;
  });

  $('form.safedirty').on('submit', function(e) {
    this.dirty = false;
  });

  $(window).on('beforeunload', function(e) {
    forms = $('form.safedirty');
    for (var i = 0; i < forms.length; i++) {
      if (forms[i].dirty) {
        e.preventDefault();
        return 'You will lose your changes!';
      }
    }
  });
});
