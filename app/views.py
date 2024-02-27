from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import generic
from . import models
# Create your views here.

class KittenListView(generic.ListView):
    model = models.Kitten
    paginate_by = 20

class KittenDetailView(generic.DetailView):
    model = models.Kitten

class KittenCreate(generic.CreateView):
    model = models.Kitten

class KittenUpdate(generic.UpdateView):
    model = models.Kitten

class KittenDelete(generic.DeleteView):
    model = models.Kitten
    