from django import forms
from .models import CookBook


class CookBookForm(forms.ModelForm):
    class Meta:
        model = CookBook
        exclude = ['ingridients']

class IngridientsForm(forms.Form):
    pass