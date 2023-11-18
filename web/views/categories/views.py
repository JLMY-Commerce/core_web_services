from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from web.models import Produto, Categoria


class CategoriesDetailView(DetailView):
    model = Categoria
    template_name = 'categories/category.html'
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categoria.objects.all()
        return context