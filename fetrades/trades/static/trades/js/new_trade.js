SCCY_ID = "#id_sell_currency"; // sell currency selector id
BCCY_ID = "#id_buy_currency"; // buy currency selector id
RATE_ID = "#id_rate"; // rate input id
SAMT_ID = "#id_sell_amount"; // sell amount input id
BAMT_ID = "#id_buy_amount"; // buy amount input id

$(SCCY_ID).on('change', function () {
    renderRate(callback = renderBuyAmount)
});

$(BCCY_ID).on('change', function () {
    renderRate(callback = renderBuyAmount)
});

$(SAMT_ID).on('change', function () {
    renderRate(callback = renderBuyAmount)
});

function renderRate(callback = null) {
    sell_ccy = $(SCCY_ID).val()
    buy_ccy = $(BCCY_ID).val()

    if (sell_ccy != "" && buy_ccy != "") {
        $.ajax({
            method: "POST",
            url: get_rate_url,
            data: {
                'sell_ccy': sell_ccy,
                'buy_ccy': buy_ccy
            },
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },
            success: function (data) {
                if (data.error !== undefined && data.error !== null) {
                    alert(data.error);
                    $(RATE_ID).val("error")
                } else {
                    $(RATE_ID).val(parseFloat(data.rate).toFixed(4))
                }
            },
            error: function (jqXHR, status, errorThrown) {
                message = "Couldn't get the rate: ";
                message += jqXHR.status + ": " + errorThrown
                alert(message);
            },
            complete: callback
        });
    } else {
        $(RATE_ID).val("")
    }
}

function renderBuyAmount() {
    rate = parseFloat($(RATE_ID).val()).toFixed(4)
    samt = parseFloat($(SAMT_ID).val()).toFixed(2)

    if (!isNaN(rate) && !isNaN(samt)) {
        amount = rate * samt
        $(BAMT_ID).val(amount.toFixed(2))
    } else {
        $(BAMT_ID).val("")
    }
}
