from django import forms


class Gipot(forms.Form):
    leg1 = forms.IntegerField(label='leg of the hypotenuse 1', min_value=1)
    leg2 = forms.IntegerField(label='leg of the hypotenuse 2', min_value=1)
