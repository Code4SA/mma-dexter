$(function() {
  $('[title]').tooltip();
  $('.select2').select2();
});

$(function() {
  var now = moment();
  var yesterday = now.clone().subtract(moment.duration(1, 'days'));

  $('.use-daterangepicker').daterangepicker({
    format: 'YYYY/MM/DD',
    opens: 'right',
    maxDate: now.clone().add(moment.duration(1, 'days')),
    ranges: {
      'Today': [now, now],
      'Yesterday': [yesterday, yesterday],
      'Last 7 days': [now.clone().subtract(moment.duration(7, 'days')), now],
      'Last 14 days': [now.clone().subtract(moment.duration(14, 'days')), now],
      'Last 30 days': [now.clone().subtract(moment.duration(30, 'days')), now],
      'Last 90 days': [now.clone().subtract(moment.duration(90, 'days')), now],
      'Elections 2014': [moment('2014-03-07'), moment('2014-05-14')]
    }
  });
});

// People and quotations
$(function () {
  var $quotations = $('.people-quotations');

  $('.people-table a, .people-table tr').on('click', function(e) {
    e.preventDefault();

    var $this = $(this),
        $row = $this.closest('tr'),
        $link = $row.find('a');

    $row.siblings('.active').removeClass('active');
    $row.addClass('active');

    $quotations.find('.in').removeClass('in');
    $($link.attr('href')).addClass('in');
  });
});
