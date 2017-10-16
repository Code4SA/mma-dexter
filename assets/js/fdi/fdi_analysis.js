/**
 * Created by mrade_000 on 13-Oct-17.
 */
$(document).ready(function () {

    $('#fdi-new-involvement_id1').on('change.select2', function () {

            var tier1 = $('#fdi-new-involvement_id1').find("option:selected").val();
            var tier2 = $('#fdi-new-involvement_id2').find("option:selected").val();

            $.getJSON('/_parse_involvement', {

                    inv_id1: tier1,
                    inv_id2: tier2

                },
                function (data) {
                    var tier2_data = data.t2;
                    var tier3_data = data.t3;

                    var options = $("#fdi-new-involvement_id2");
                    options.empty();
                    tier2_data.forEach(function (item) {
                        options.append($('<option>', {value: item[0], text: item[1]}));
                    });

                    var options2 = $("#fdi-new-involvement_id3");
                    options2.empty();
                    tier3_data.forEach(function (item) {
                        options2.append($('<option>', {value: item[0], text: item[1]}));
                    });

                    $('#fdi-new-involvement_id2').val(73).trigger('change.select2');
                    $('#fdi-new-involvement_id3').val(19).trigger('change.select2');

            });

        });

$('#fdi-new-involvement_id2').on('change.select2', function () {

            var tier1 = $('#fdi-new-involvement_id1').find("option:selected").val();
            var tier2 = $('#fdi-new-involvement_id2').find("option:selected").val();

            $.getJSON('/_parse_involvement', {

                    inv_id1: tier1,
                    inv_id2: tier2

                },
                function (data) {
                    var tier2_data = data.t2;
                    var tier3_data = data.t3;

                    var options = $("#fdi-new-involvement_id2");
                    options.empty();
                    tier2_data.forEach(function (item) {
                        options.append($('<option>', {value: item[0], text: item[1]}));
                    });

                    var options2 = $("#fdi-new-involvement_id3");
                    options2.empty();
                    tier3_data.forEach(function (item) {
                        options2.append($('<option>', {value: item[0], text: item[1]}));
                    });

                    $('#fdi-new-involvement_id3').val(19).trigger('change.select2');

            });

        });

});