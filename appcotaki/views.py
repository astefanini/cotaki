from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render
from django.template import RequestContext
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from appcotaki.forms import CotacaoCreateForm
from appcotaki.models import (Clientes, Comissoes, Cotacoes, Fabricantes,
                              Materiais, Pedidos)

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


class ComissaoCreateView(CreateView):
    template_name = "comissao_create.html"
    model = Comissoes
    fields = [
        'percentual',
    ]
    success_url = reverse_lazy("comissao_list_todos")


class ComissaoListView(ListView):
    template_name = "comissao_list_todos.html"
    model = Comissoes
    context_object_name = "comissao_list"


class FabricanteCreateView(CreateView):
    template_name = "fabricante_create.html"
    model = Fabricantes
    fields = [
        'nome',
        'produto',
    ]
    success_url = reverse_lazy("fabricante_list_todos")


class FabricanteListView(ListView):
    template_name = "fabricante_list_todos.html"
    model = Fabricantes
    context_object_name = "fabricante_list"


class MaterialCreateView(CreateView):
    template_name = "material_create.html"
    model = Materiais
    fields = [
        'nome',
        'um',
        'precoUnit',
    ]
    success_url = reverse_lazy("Material_list_todos")


class MaterialListView(ListView):
    template_name = "material_list_todos.html"
    model = Materiais
    context_object_name = "material_list"


def CotacaoCreate(request):

    # Cria form
    form = CotacaoCreateForm(request.POST or None)

    # Valida e salva
    if form.is_valid():
        salvar = form.save(commit=False)
        salvar.save()
        return HttpResponse("Dados inseridos com sucesso!")

    # Chama Template
    return render(request, 'cotacao_create.html', context)

# class CotacaoCreateView(CreateView):
#    template_name = "cotacao_create.html"
#    model = Cotacoes
#    fields = [
#        'numCotacao',
#        'data',
#        'nomeFabricante',
#        'tipoMaterial',
#        'umMaterial',
#        'qtdMaterial',
#        'statusCotacao',
#        'motivoReprovacao',
#        'nomCliente',

#    success_url = reverse_lazy("cliente_list_todos")


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


def PedidoClienteListView(request, nom_cliente):
    # Cria um objeto vazio chamado cotacoes
    pedidos_list = None

    # Aplica o filtro sobre os objetos em Cliente
    v_pedidos_filtrado = Pedidos.objects.filter(nomCliente=nom_cliente)

    # Verifica se foi encontrado algum registro
    if len(v_pedidos_filtrado) > 0:
        pedidos_list = v_pedidos_filtrado
    else:
        pedidos_list = None

    # Retorna o template clientes_lista.html e passa o filtro como parâmetro
    return render(request, 'pedido_cliente_list.html', {'pedidos_list': pedidos_list, })
