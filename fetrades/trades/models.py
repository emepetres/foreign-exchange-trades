from django.db import models
from django.forms.models import model_to_dict
from django.utils.crypto import get_random_string

from trades.currency_codes import CURRENCY_CODES


def _build_id():
    return 'TR' + get_random_string(7).upper()


class Trade(models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=9,
        default=_build_id)

    sell_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CODES)
    sell_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2)

    buy_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CODES)
    buy_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2)

    rate = models.DecimalField(
        max_digits=6,
        decimal_places=4)

    date_booked = models.DateTimeField(
        auto_now_add=True)

    def to_dict(self):
        response = model_to_dict(self)
        response['date_booked'] = self.date_booked
        return response

    @classmethod
    def list_all(cls, return_queryset=False):
        trade_list = []
        try:
            trade_list = cls.objects.all()
        except cls.DoesNotExist:
            pass

        if return_queryset:
            return trade_list
        else:
            return [item.to_dict() for item in trade_list]
