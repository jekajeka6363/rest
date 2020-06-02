from django import forms
from rest.apps.main.models import Restorant
from django.core.exceptions import ValidationError

class RestourantForm(forms.Form):
    name_restorant = forms.CharField(label="Название рестрорана", max_length=20)
    rescription_restorant = forms.CharField(label="Описание ресторана",max_length=200)
    rating_restorant = forms.IntegerField(label="Рейтинг")

    def clean_name_restorant(self):
        new_name_restorant = self.cleaned_data["name_restorant"].lower()
        if Restorant.objects.filter(name_restorant=new_name_restorant).count() > 0:
            raise ValidationError("Ресторан уже добавлен")
        return new_name_restorant

    def save(self):
        new_rest = Restorant.objects.create(name_restorant=self.cleaned_data["name_restorant"],
                                            rescription_restorant=self.cleaned_data["rescription_restorant"],
                                            rating_restorant=self.cleaned_data["rating_restorant"])
        return new_rest

