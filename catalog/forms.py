from django import forms
from django.forms import ModelForm
from .models import Person


class Gipot(forms.Form):
    leg1 = forms.IntegerField(label='leg of the hypotenuse 1', min_value=1)
    leg2 = forms.IntegerField(label='leg of the hypotenuse 2', min_value=1)


class Pers(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']


