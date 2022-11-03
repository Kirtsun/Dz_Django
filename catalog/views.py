from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import Gipot, PersonForm
from .models import Person


@require_http_methods(['GET', ])
def triangle(request):
    if 'Submit' in request.GET:
        form = Gipot(request.GET)
        if form.is_valid():
            leg1 = form.cleaned_data['leg1']
            leg2 = form.cleaned_data['leg2']
            res = (leg1 ** 2 + leg2 ** 2) ** .5
            res = round(res, 2)
            return render(request, "catalog/triangle.html", {'res': res})
    else:
        form = Gipot()
    return render(request, "catalog/triangle.html", {"form": form})


def person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
            return redirect('catalog:person')
    else:
        form = PersonForm()
    return render(request, 'catalog/create_person.html', {'form': form})

