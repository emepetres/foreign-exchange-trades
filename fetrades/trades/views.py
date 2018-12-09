import json

import requests
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from fetrades import settings
from trades.models import Trade

from .forms import TradeForm


def trades(request):
    context = {
        'webname': settings.WEBNAME,
        'trades_list': Trade.list_all(return_queryset=True)
    }

    return render(request, 'trades.html', context)


def new_trade(request):
    # if POST call, process data, else render the form
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            # NOTE: recheck that values are the same than in fixer.io
            form.save()
            return HttpResponseRedirect(reverse('trades'))
    else:
        form = TradeForm()

    context = {
        'webname': settings.WEBNAME,
        'form': form
    }

    return render(request, 'new_trade.html', context)


def get_rate(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'The request only allows POST'})

    sell_ccy = request.POST.get('sell_ccy', None)
    if not sell_ccy or sell_ccy == "":
        return JsonResponse({'error': 'No sell currency provided'})

    buy_ccy = request.POST.get('buy_ccy', None)
    if not buy_ccy or buy_ccy == "":
        return JsonResponse({'error': 'No buy currency provided'})

    url = 'http://data.fixer.io/api/latest?access_key=' + \
        settings.FIXER_API_KEY
    # currencies
    url += '&base=' + sell_ccy
    url += '&symbols=' + buy_ccy

    # get data from fixer.io
    data = json.loads(requests.request("GET", url).text)

    if 'success' not in data \
            or ('rates' not in data and 'error' not in data):
        return JsonResponse({'error': 'Unexpected response from fixer.io'})

    if data['success']:
        return JsonResponse({'rate': data['rates'][buy_ccy]})
    else:
        return JsonResponse({'error': data['error']['type']})
