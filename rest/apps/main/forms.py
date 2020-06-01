from django import forms
from .models import Restorant

class NameForm(forms.Form):
    name_restorant = forms.CharField(label="Название рестрорана", max_length=20)
    rescription_restorant = forms.CharField(label="Описание ресторана",max_length=200)
    rating_restorant = forms.IntegerField(label="Рейтинг")
