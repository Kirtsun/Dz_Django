from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import Gipot


def index(request):
    return render(request, "catalog/index.html")


@require_http_methods(['GET', ])
def triangle(request):
    if 'Submit' in request.GET:
        form = Gipot(request.GET)
        if form.is_valid():
            leg1 = int(request.GET.get("leg1"))
            leg2 = int(request.GET.get("leg2"))
            res = (leg1 ** 2 + leg2 ** 2) ** .5
            res = round(res, 2)
            return render(request, "catalog/triangle.html", {'res': res})
    else:
        form = Gipot()
        return render(request, "catalog/triangle.html", {"form": form})
