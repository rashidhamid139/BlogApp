from django.shortcuts import render
import requests
from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    intitle = 'TypeError: an integer is required'

    
    url = 'https://api.stackexchange.com/2.2/search'
    headers = { 'User-Agent': 'github.com/vitorfs/seot' }
    params = {
        'order': 'desc',
        'sort': 'votes',
        'site': 'stackoverflow',
        'pagesize': 3,
        'tagged': 'python;django',
        'intitle': intitle
    }
    r = requests.get(url, params=params, headers=headers)
    questions = r.json()


    context = {'questions': questions}
    return render(request, "middleware_demo/index.html", context)