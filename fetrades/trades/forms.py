from django.forms import ModelForm
from trades.models import Trade


class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = [
            'sell_currency',
            'sell_amount',
            'buy_currency',
            'buy_amount',
            'rate'
        ]
