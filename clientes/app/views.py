from django.shortcuts import render
from django.views.generic import CreateView,ListView, UpdateView
from .models import Cliente

class ClienteCreateView(CreateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_cliente.html"
    success_url = "lista_clientes"

class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"

class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = "__all__"
    template_name = "form_cliente.html"
    succes_url = reverse_lazy("lista_clientes")
