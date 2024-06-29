from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm
from django.shortcuts import get_object_or_404
from outflows.models import Outflow


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'
    paginate_by = 10


class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_create.html'
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'client_update.html'
    form_class = ClientForm
    success_url = reverse_lazy('client_list')


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'



class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client_id = self.kwargs.get('pk')  # Assume que 'pk' é a chave primária na URL
        client = get_object_or_404(Client, pk=client_id)
        
        # Verifica se existem outflows associados ao cliente
        outflows_exist = Outflow.objects.filter(client=client).exists()
        
        # Adiciona a informação ao contexto
        context['outflows_exist'] = outflows_exist
        return context