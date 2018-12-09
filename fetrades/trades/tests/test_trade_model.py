from django.test import TestCase
from trades.models import Trade


class TradeTestCase(TestCase):
    def setUp(self):
        Trade.objects.create(
            sell_currency='EUR',
            sell_amount=23.50,
            buy_currency='GBP',
            buy_amount='18.05',
            rate=0.9621
        )
        Trade.objects.create(
            sell_currency='GBP',
            sell_amount=1205.50,
            buy_currency='USD',
            buy_amount='1023.89',
            rate=0.9801
        )
        Trade.objects.create(
            sell_currency='USD',
            sell_amount=200.00,
            buy_currency='EUR',
            buy_amount='206.50',
            rate=1.0325
        )

    def test_id_generation(self):
        """All id are composed by 'TR' + 7 alphanumerics"""
        queryset = Trade.objects.all()

        self.assertGreater(len(queryset), 0)

        for item in queryset:
            self.assertRegex(item.id, 'TR\w{7,7}')

    def test_list_all(self):
        """Retrieve all trades ordered by date booked"""
        queryset = Trade.list_all()

        self.assertEqual(len(queryset), 3)

        last_timestamp = 0
        for item in queryset:
            self.assertGreater(item['date_booked'].timestamp(), last_timestamp)
            last_timestamp = item['date_booked'].timestamp()

    def test_list_all_queryset(self):
        """Retrieve all trades ordered by date booked"""
        queryset = Trade.list_all(return_queryset=True)

        self.assertEqual(len(queryset), 3)

        last_timestamp = 0
        for item in queryset:
            self.assertGreater(item.date_booked.timestamp(), last_timestamp)
            last_timestamp = item.date_booked.timestamp()
