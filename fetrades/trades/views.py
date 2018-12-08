from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from trades.models import Trade

from .forms import TradeForm


def landing(request):
    context = {
        'trades_list': Trade.list_all(return_queryset=True)
    }

    return render(request, 'trades.html', context)


def new_trade(request):
    # if POST call, process data, else render the form
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            # TODO recheck that values are the same than in fixer.io
            form.save()
            return HttpResponseRedirect(reverse('trades'))
    else:
        form = TradeForm()

    return render(request, 'new_trade.html', {'form': form})
