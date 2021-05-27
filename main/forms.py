from django import forms
from main.models import City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ('lat', 'lon')