from django import forms
from django.shortcuts import render
from .models import  CookBook
from .forms import CookBookForm,IngridientsForm
import json
# Create your views here.
def dynamic(request):
    content = {}
    context = {}

    ckb = CookBook.objects.last()
    print(request.method)
    if ckb == None:
        print(ckb)
        ckb = CookBook.objects.create()
    
    if request.method == 'POST':
        if 'recipe_name' in request.POST:
            ckb.recipe_name = int(request.POST['recipe_name'])
            ckb.save()

        try:
            content = json.loads(ckb.ingridients)
        except json.JSONDecodeError:
            content = {}

    else:
        for key in request.POST.keys():
            if key != 'csrfmiddlewaretoken':
                content[key] = request.POST[key]
            ckb.ingridients = json.dumps(content)
            ckb.save()

    if ckb.recipe_name == 0:
        new_fields = {
            'cheese': forms.IntegerField(),
            'ham'   : forms.IntegerField(),
            'onion' : forms.IntegerField(),
            'bread' : forms.IntegerField(),
            'ketchup': forms.IntegerField()}
    else:
        new_fields = {
            'milk'  : forms.IntegerField(),
            'butter': forms.IntegerField(),
            'honey' : forms.IntegerField(),
            'eggs'  : forms.IntegerField()}

    DynamicIngridientsForm = type('DynamicIngridientsForm', (IngridientsForm,), new_fields)
    IngForm = DynamicIngridientsForm(content)
    context['ingridients_form'] = IngForm
    context['cookbook_form']    = CookBookForm(request.POST or None)
    return render(request, "dynamic/nondynamic.html", context)