from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from . import models
# Create your views here.

class KittenListView(generic.ListView):
    model = models.Kitten


class KittenDetailView(generic.DetailView):
    model = models.Kitten