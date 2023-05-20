from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from Recetas.models import MundoRecetas
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy




def index(request):
    return render(request , 'Recetas/index.html')


class MundoRecetasList(ListView):
    model = MundoRecetas
    context_object_name = 'nombres'


class MundoRecetasDetail(DetailView):
    model = MundoRecetas
    context_object_name = 'nombre' 


class MundoRecetasUpdate(UpdateView):
    model = MundoRecetas
    success_url = reverse_lazy('recetas-list')
    fields = '__all__'


class MundoRecetasDelete(DeleteView):
    model = MundoRecetas
    success_url = reverse_lazy('recetas-list')
    context_object_name = 'nombre'


class MundoRecetasCreate(CreateView):
    model = MundoRecetas
    success_url = reverse_lazy('recetas-list')
    fields = '__all__'


class MundoRecetasSearch(ListView):
    model = MundoRecetas
    context_object_name = 'nombres'                                                              # Si no definimos el context queda por defecti objects_list , y no nos imprimira
    

    def get_queryset(self):
        criterio = self.request.GET.get('criterio')
        resultado = MundoRecetas.objects.filter(nombre__icontains=criterio).all()
        return resultado 


         

    

