from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from appcotaki.models import (Clientes, Comissoes, Cotacoes, Fabricantes,
                              Materiais, Pedidos)

# from appcotaki.forms import TransporteCreateForm
# from appcotaki.forms import ContratoCreateForm

# Create your views here.


class ClienteCreateView(CreateView):
    template_name = "cliente_create.html"
    model = Clientes
    fields = [
        'nome',
    ]
    success_url = reverse_lazy("cliente_list_todos")


class ClienteListView(ListView):
    template_name = "cliente_list_todos.html"
    model = Clientes
    context_object_name = "cliente_list"


def CotacaoClienteListView(request, nom_cliente):
    # Cria um objeto vazio chamado cotacoes
    cotacoes_list = None

    # Aplica o filtro sobre os objetos em Cliente
    v_cotacoes_filtrado = Cotacoes.objects.filter(nomCliente=nom_cliente)

    # Verifica se foi encontrado algum registro
    if len(v_cotacoes_filtrado) > 0:
        cotacoes_list = v_cotacoes_filtrado
    else:
        cotacoes_list = None

    # Retorna o template clientes_lista.html e passa o filtro como parâmetro
    return render(request, 'cotacao_cliente_list.html', {'cotacoes_list': cotacoes_list, })
