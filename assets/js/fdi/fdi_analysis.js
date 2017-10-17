/**
 * Created by mrade_000 on 13-Oct-17.
 */
$(document).ready(function () {

    $('#fdi-new-involvement_id1').on('change.select2', function () {

            var tier1 = $('#fdi-new-involvement_id1').find("option:selected").val();
            var tier2 = $('#fdi-new-involvement_id2').find("option:selected").val();
            var tier3 = $('#fdi-new-involvement_id3').find("option:selected").val();

            $.getJSON('/_parse_involvement', {

                    inv_id1: tier1,
                    inv_id2: tier2,
                    inv_id3: tier3,
                    tier1_change: "1",
                    tier2_change: "0",
                    tier3_change: "0"

                },
                function (data) {
                    var tier2_data = data.t2;
                    var tier3_data = data.t3;
                    var ti2 = data.ti2;
                    var ti3 = data.ti3;

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

                    $('#fdi-new-involvement_id2').val(ti2).trigger('change.select2');
                    $('#fdi-new-involvement_id3').val(ti3).trigger('change.select2');
                    $('#fdi-new-involvement_id3 option[value=ti3]').attr('selected', 'selected');
                    // $('#fdi-new-involvement_id2').val("73");
                    // $('#fdi-new-involvement_id3').val("19");
                    // $('#fdi-new-involvement_id2 option[value="73"]').attr('value', '73');
                    // $('#fdi-new-involvement_id2 option[value="73"]').attr('selected', 'selected');
                    // $('#fdi-new-involvement_id3 option[value="19"]').attr('value', '19');
                    // $('#fdi-new-involvement_id3 option[value="19"]').attr('selected', 'selected');

            });

        });

$('#fdi-new-involvement_id2').on('change.select2', function () {

            var tier1 = $('#fdi-new-involvement_id1').find("option:selected").val();
            var tier2 = $('#fdi-new-involvement_id2').find("option:selected").val();
            var tier3 = $('#fdi-new-involvement_id3').find("option:selected").val();

            $.getJSON('/_parse_involvement', {

                    inv_id1: tier1,
                    inv_id2: tier2,
                    inv_id3: tier3,
                    tier1_change: "0",
                    tier2_change: "1",
                    tier3_change: "0"

                },
                function (data) {
                    var tier3_data = data.t3;
                    var ti3 = data.ti3;

                    var options2 = $("#fdi-new-involvement_id3");
                    options2.empty();
                    tier3_data.forEach(function (item) {
                        options2.append($('<option>', {value: item[0], text: item[1]}));
                        console.log(item)
                    });

                    $('#fdi-new-involvement_id3').val(ti3).trigger('change.select2');
                    $('#fdi-new-involvement_id3 option[value=ti3]').attr('selected', 'selected');

            });

        });

$('#fdi-new-involvement_id3').on('change.select2', function () {

            var tier1 = $('#fdi-new-involvement_id1').find("option:selected").val();
            var tier2 = $('#fdi-new-involvement_id2').find("option:selected").val();
            var tier3 = $('#fdi-new-involvement_id3').find("option:selected").val();

            $.getJSON('/_parse_involvement', {

                    inv_id1: tier1,
                    inv_id2: tier2,
                    inv_id3: tier3,
                    tier1_change: "0",
                    tier2_change: "0",
                    tier3_change: "1"

                },
                function (data) {
                    var tier3_data = data.t3;
                    var ti3 = data.ti3;

                    var options2 = $("#fdi-new-involvement_id3");
                    options2.empty();
                    tier3_data.forEach(function (item) {
                        options2.append($('<option>', {value: item[0], text: item[1]}));
                        console.log(item)
                    });

                    $('#fdi-new-involvement_id3').val(ti3);
                    $('#fdi-new-involvement_id3 option[value=ti3]').attr('value', ti3);
                    $('#fdi-new-involvement_id3 option[value=ti3]').attr('selected', 'selected');

            });

        });

});