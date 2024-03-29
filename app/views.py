from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from . import models
# Create your views here.

class KittenListView(generic.ListView):
    model = models.Kitten
    queryset = models.Kitten.objects.all().order_by('pk')
    paginate_by = 20

    def get(self, request, *args, **kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return self.get_json_response()
        else:
            return super().get(request, *args, **kwargs)

    def get_json_response(self):
        fields = ['name', 'age', 'cuteness', 'softness']
        data = {
            'kittens': list(self.get_queryset().values(*fields)),
        }
        return JsonResponse(data)

class KittenDetailView(generic.DetailView):
    model = models.Kitten

    def get(self, request, *args, **kwargs):
        if self.request.headers.get('Accept') == 'application/json':
            return self.get_json_response()
        else:
            return super().get(request, *args, **kwargs)

    def get_json_response(self):
        fields = ['name', 'age', 'cuteness', 'softness']
        data = {field: getattr(self.get_object(), field) for field in fields}
        return JsonResponse(data)

class KittenCreate(generic.CreateView):
    model = models.Kitten
    fields = ['name', 'age', 'cuteness', 'softness']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Kitten created successfully!')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error creating kitten. Please check the form.')
        return super().form_invalid(form)

class KittenUpdate(generic.UpdateView):
    model = models.Kitten
    fields = ['name', 'age', 'cuteness', 'softness']

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Kitten updated successfully!')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error updating kitten. Please check the form.')
        return super().form_invalid(form)

class KittenDelete(generic.DeleteView):
    model = models.Kitten
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Kitten deleted successfully!')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error deleting kitten.')
        return super().form_invalid(form)