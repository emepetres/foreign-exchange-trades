from decimal import Decimal
from django.db import models
from django.forms.models import model_to_dict
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator

from trades.currency_codes import CURRENCY_CODES


def _build_id():
    """Builds a new id of type 'TR' + 7 alphanumerics"""
    return 'TR' + get_random_string(7).upper()


class Trade(models.Model):
    """Model of a single foreign exchange trade"""
    id = models.CharField(
        primary_key=True,
        max_length=9,
        default=_build_id)

    sell_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CODES)
    sell_amount = models.DecimalField(  # > 0.01
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])

    buy_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CODES)
    buy_amount = models.DecimalField(  # > 0.01
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))])

    rate = models.DecimalField(  # > 0.0001
        max_digits=10,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0001'))])

    date_booked = models.DateTimeField(  # auto, current timestamp
        auto_now_add=True)

    def to_dict(self):
        response = model_to_dict(self)
        response['date_booked'] = self.date_booked
        return response

    @classmethod
    def list_all(cls, return_queryset=False):
        trade_list = cls.objects.all()

        if return_queryset:
            return trade_list
        else:
            return [item.to_dict() for item in trade_list]

    @classmethod
    def _build_id(cls):
        """Builds a new unique id of type 'TR' + 7 alphanumerics

        NOTE: Cannot be used as primary key generator because full class
        definition is needed beforehand.
        """
        while True:
            new_id = 'TR' + get_random_string(7).upper()
            try:
                cls.objects.get(new_id)
                continue
            except cls.DoesNotExist:
                return new_id

    def __str__(self):
        return "[{}] {}{}->{}{}, rate {} | {}".format(
            self.id,
            self.sell_amount,
            self.sell_currency,
            self.buy_amount,
            self.buy_currency,
            self.rate,
            self.date_booked)
