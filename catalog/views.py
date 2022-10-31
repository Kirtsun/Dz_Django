
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Gipot


def index(request):
    return HttpResponse("Hello. You're at the catalog index.")


def triangle(request):
    form = Gipot()
    if 'Done' in request.GET:
        form = Gipot(request.GET)
        if form.is_valid():
            leg1 = int(request.GET.get("leg1"))
            leg2 = int(request.GET.get("leg2"))
            print(type(leg1))
            res = (leg1 ** 2 + leg2 ** 2) ** .5
            return redirect(request, "catalog/triangle.html", {"res": res})
    return render(request, "catalog/triangle.html", {"form": form})


