from django.http import HttpResponseRedirect
from django.shortcuts import render

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
        if 'cancel' in request.POST:
            return HttpResponseRedirect('/')  # FIXME
        form = TradeForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect('/')  # FIXME
    else:
        form = TradeForm()

    return render(request, 'new_trade.html', {'form': form})
