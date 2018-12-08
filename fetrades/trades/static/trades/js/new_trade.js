SCCY_ID = "#id_sell_currency"; // sell currency selector id
BCCY_ID = "#id_buy_currency"; // buy currency selector id
RATE_ID = "#id_rate"; // rate input id
SAMT_ID = "#id_sell_amount"; // sell amount input id
BAMT_ID = "#id_buy_amount"; // buy amount input id

$(SCCY_ID).on('change', function () {
    renderRate()
    renderBuyAmount()
});

$(BCCY_ID).on('change', function () {
    renderRate()
    renderBuyAmount()
});

$(SAMT_ID).on('change', function () {
    renderBuyAmount()
});

function renderRate() {
    sell_ccy = $(SCCY_ID).val()
    buy_ccy = $(BCCY_ID).val()

    if (sell_ccy != "" && buy_ccy != "") {
        $(RATE_ID).val(8) // TODO connect with fixer.io
    } else {
        $(RATE_ID).val("")
    }
}

function renderBuyAmount() {
    rate = parseInt($(RATE_ID).val())
    samt = parseInt($(SAMT_ID).val())

    console.log(rate)
    console.log(samt)
    if (!isNaN(rate) && !isNaN(samt)) {
        $(BAMT_ID).val(rate * samt)
    } else {
        $(BAMT_ID).val("")
    }
}