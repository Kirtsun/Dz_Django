from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods


from .forms import Gipot, PersonForm
from .models import Person


def index(request):
    latest_person_list = Person.objects.all()
    context = {'latest_person_list': latest_person_list}
    return render(request, 'catalog/index.html', context)


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
            form.save()
            return redirect('catalog:index')
    else:
        form = PersonForm()
    return render(request, 'catalog/create_person.html', {'form': form})


def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('catalog:index')
    else:
        form = PersonForm(instance=person)
    return render(request, 'catalog/update_person.html', {'form': form})
