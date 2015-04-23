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

  $('.people-table').on('click', 'a, tr', function(e) {
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

$(function() {
  // people search/filter
  var people = $('.people-table tr[data-id]').map(function(i) {
    return {
      id: $(this).data('id'),
      text: $(this).find('.name').text(),
    };
  }).toArray();

  var filterBox = $('.person-filter-box');

  filterBox.select2({
    placeholder: 'Find a person',
    allowClear: true,
    minimumInputLength: 3,
    data: people,
    ajax: {
      url: '/api/people',
      data: function (term, page) {
        return {
          q: term, // search term
        };
      },
      results: function(data, page, query) {
        return {
          more: data.length == 10,
          results: $.map(data.people, function(item) {
            return {
              id: item.id,
              text: item.name,
            };
          })
        };
      },
    }
  });

  // user chose a person
  filterBox.on('change', function(e) {
    var data = filterBox.select2('data');
    if (!data) return;

    var personId = data.id,
        name = data.text;

    // is the person already in the table?
    var row = $('.people-table tr[data-id=' + personId + ']');
    if (row.length > 0) {
      // click it
      $(row).click();

    } else {
      // insert a new row and load the data
      var first = $('.people-table tr[data-id]').first();
      var template = first.clone();

      template.attr('data-id', personId);
      template.find('td:eq(0)').html('<i class="fa fa-spinner fa-pulse"></i>');
      template.find('td:eq(1)').text(name);
      template.find('td:eq(2), td:eq(3), td:eq(4)').html('');

      first.before(template.clone());
      filterBox.select2('val', '');

      // kick off the loader
      loadPersonData(personId);
    }
  });

  function loadPersonData(personId) {
    // load the person row and the utterances from the server
    var url = '/mine/person/' + personId + document.location.search;

    $.get(url)
      .then(function(data) {
        var template = $('.people-table tr[data-id=' + personId + ']');

        if (data.utterances) {
          $('.people-quotations').append(data.utterances);
        }

        if (data.row) {
          template.replaceWith(data.row);
          // get the new nodes
          template = $('.people-table tr[data-id=' + personId + ']');
          template.find('*[data-sparkline]').sparkline();
        }

        template.click();
        initQuotations($('#quotations-' + personId + ' .quote'));
      });
  }
});

// media
$(function() {
  $('.medium').on('click', function(e) {
    e.preventDefault();

    var $this = $(this),
        $link = $this.find('a');

    document.location = $link.attr('href');

  });
});

// show spinner
$(function() {
  $('.dates a, .media a').click(function() {
    $('.fa-spinner').removeClass('hidden');
  });
});

function initQuotations(elems) {
  elems
    .each(function(i) {
      $(this).popover({
        content: $(this).data('snippet'),
        html: true,
        placement: 'top auto',
      });
    })
    .on('mouseover', function() {
      $(this).popover('show');
    })
    .on('mouseout', function() {
      $(this).popover('hide');
    });
}

// show popover with quote context
$(function() {
  initQuotations($('.people-quotations .quote'));
});
