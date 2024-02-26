from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from . import models
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    context = {
        'kittens': models.Kitten.objects.all(),
    }
    return render(request=request, template_name='index.html', context=context)