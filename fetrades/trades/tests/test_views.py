import json
from django.test import TestCase, Client
from trades.models import Trade
from django.urls import reverse


class ViewsTestCase(TestCase):

    def test_trades_render(self):
        """Trades page is reachable and renders as expected"""
        c = Client()
        response = c.get(
            reverse('trades')
        )
        self.assertEqual(response.status_code, 200)

    def test_new_trade_render(self):
        """New trade page is reachable and renders as expected"""
        c = Client()
        response = c.get(
            reverse('new_trade')
        )
        self.assertEqual(response.status_code, 200)

    def test_new_trade_post_valid(self):
        """It can create a new trade"""
        previous_length = len(Trade.objects.all())

        c = Client()
        response = c.post(
            reverse('new_trade'),
            {
                'sell_currency': ['EUR'],
                'sell_amount': ['78.94'],
                'rate': ['12345'],
                'buy_currency': ['USD'],
                'buy_amount': ['89.85']
            }
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(previous_length+1, len(Trade.objects.all()))

    def test_new_trade_post_invalid_ccy(self):
        """Cannot create trade if ccy is invalid"""
        previous_length = len(Trade.objects.all())

        c = Client()
        response = c.post(
            reverse('new_trade'),
            {
                'sell_currency': ['EURA'],
                'sell_amount': ['78.94'],
                'rate': ['12345'],
                'buy_currency': ['USD'],
                'buy_amount': ['89.85']
            }
        )
        self.assertEqual(response.status_code, 200)

        self.assertEqual(previous_length, len(Trade.objects.all()))

    def test_new_trade_post_invalid_amount(self):
        """Cannot create trade if amount is invalid"""
        previous_length = len(Trade.objects.all())

        c = Client()
        response = c.post(
            reverse('new_trade'),
            {
                'sell_currency': ['EUR'],
                'sell_amount': ['78.94'],
                'rate': ['12345'],
                'buy_currency': ['USD'],
                'buy_amount': ['-7']
            }
        )
        self.assertEqual(response.status_code, 200)

        self.assertEqual(previous_length, len(Trade.objects.all()))

    def test_get_rate(self):
        """Latest rate info can be retrieved"""
        c = Client()
        response = c.post(
            reverse('get_rate'),
            {
                'sell_ccy': 'EUR',
                'buy_ccy': 'USD'
            }
        )
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)

        self.assertTrue('error' not in data or data['error'] == "")
        self.assertTrue('rate' in data)
        self.assertTrue(isinstance(data['rate'], float))
