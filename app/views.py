from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views import generic
from . import models
# Create your views here.

class KittenListView(generic.ListView):
    model = models.Kitten
    queryset = models.Kitten.objects.all().order_by('pk')
    paginate_by = 20

class KittenDetailView(generic.DetailView):
    model = models.Kitten

class KittenCreate(generic.CreateView):
    model = models.Kitten
    fields = ['name', 'age', 'cuteness', 'softness']

class KittenUpdate(generic.UpdateView):
    model = models.Kitten
    fields = ['name', 'age', 'cuteness', 'softness']

class KittenDelete(generic.DeleteView):
    model = models.Kitten
    success_url = reverse_lazy('index')
    