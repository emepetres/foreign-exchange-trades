from django.shortcuts import render
from trades.models import Trade


def landing(request):
    context = {
        'trades_list': Trade.list_all(return_queryset=True)
    }

    return render(request, 'trades.html', context)
