from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.http import HttpResponse


#Не полная информация о товаре
class StoreListView(ListView):
    template_name = 'store_list.html'
    queryset = models.Store.objects.all()

    def get_queryset(self):
        return models.Store.objects.all()


#полная информация об товаре
class StoreDetailView(DetailView):
    template_name = 'store_detail.html'

    def get_object(self, **kwargs):
        store_id = self.kwargs.get('id')
        return get_object_or_404(models.Store, id=store_id)
