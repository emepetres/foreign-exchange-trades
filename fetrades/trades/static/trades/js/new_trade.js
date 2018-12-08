$("#id_rate").val(1)
$("#id_sell_amount").val(2)
$("#id_buy_amount").val(2)

$("#id_sell_currency").on('change', function () {
    console.log('sell currency changed!');
});

$("#id_sell_amount").on('change', function () {
    console.log('sell amount changed!');
});

$("#id_buy_currency").on('change', function () {
    console.log('buy currency changed!');
});