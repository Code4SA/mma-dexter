$(function() {
  $('[title]').tooltip();
  $('.chosen-select').chosen();

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
  // affix article text in document view
  var $text = $('.document-container .article-text');
  if ($text.length > 0) {
    $text.affix({
      offset: {
        top: $text.offset().top - 20,
      }
    });
  }
});

$(function() {
  // helper to setup the offset adjustments for hilighting
  // portions of the article
  var $article = $('.document-container .article-text');

  if ($article.length > 0) {
    var originalText = $article.data('original');

    var htmlEscape = function(str) {
      return String(str)
      .replace(/&/g, '&amp;')
      .replace(/"/g, '&quot;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
    };

    var highlightOffsets = function(offsets) {
      var text = originalText;
      var accumulatedOffset = 0;

      for (var i = 0; i < offsets.length; i++) {
        var offset = offsets[i];
        offset[0] += i * 13;

        text = text.slice(0, offset[0]) +
          '<mark>' + text.slice(offset[0], offset[0]+offset[1]) + '</mark>' +
          text.slice(offset[0]+offset[1]);
      }

      // Do HTML escape and unescape the mark tags. This technically lets
      // someone inject mark tags, but we're okay with that, it makes this easy.
      text = htmlEscape(text)
      .replace(/\&lt;mark\&gt;/g, '<mark>')
      .replace(/\&lt;\/mark&gt;/g, '</mark>')
      // now add <br> in the same way the server does
      .replace(/\n+/g, "\n")
      .replace(/\n/g, "\n")
      .replace(/\n/g, "</p>");

      $article.html('<p>' + text + '</p>');
    };

    var highlightEntities = function(container) {
      var $elems;

      if ($(container).data('offsets')) {
        $elems = $(container);
      } else {
        $elems = $('[data-offsets]', $(container));
      }

      var offsets = $.makeArray($elems.map(function(i, row) { return $(row).data('offsets'); }));
      if (offsets.length > 0) {
        offsets = offsets.join(' ').trim().split(/ +/);
        offsets = $.map(offsets, function(e) {
          var pair = e.split(':');
          return [[parseInt(pair[0]), parseInt(pair[1])]];
        });

        offsets.sort(function(a, b) { return a[0] - b[0]; });

        // coalesce overlapping offsets
        var coalesced = [offsets[0]];

        for (var i = 1; i < offsets.length; i++) {
          var prev = coalesced[coalesced.length-1];
          var curr = offsets[i];

          if (curr[0] <= prev[0] + prev[1]) {
            prev[1] = Math.max(prev[0] + prev[1], curr[0] + curr[1]) - prev[0];
          } else {
            coalesced.push(curr);
          }
        }

        offsets = coalesced;
      }

      highlightOffsets(offsets);
    };

    $('.document-container .tabs a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
      // highlight entities for the active pane
      highlightEntities($($(e.target).attr('href')));
    });

    $('.document-container .table.entities tr').on('mouseover', function(e) {
      highlightEntities($(this));
    });

    $('.document-container .table.entities tr').on('mouseout', function(e) {
      highlightEntities($('.document-container .tab-pane.active'));
    });

    highlightEntities($('.document-container .tab-pane.active'));
  }
});
