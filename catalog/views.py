from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

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


def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            pers = form.save()
            return redirect('catalog:person_create')
    else:
        form = PersonForm()
    return render(request, 'catalog/create_person.html', {'form': form})


def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            pers = form.save()
            return redirect('catalog:person_create')
    else:
        form = PersonForm(instance=person)
    return render(request, 'catalog/update_person.html', {'form': form})


