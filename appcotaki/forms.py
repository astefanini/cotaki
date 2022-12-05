from django import forms

from appcotaki.models import Clientes, Cotacoes, Fabricantes, Materiais

# from django.forms import extras


# Cria classe do form para o modelo
class CotacaoCreateForm(forms.ModelForm):

    # Define Widgets
    numCotacao = forms.IntegerField
    data = forms.DateField(required=True)
    nomeFabricante = forms.ModelChoiceField(
        queryset=Fabricantes.objects.all().order_by('nome'), widget=forms.Select)
    tipoMaterial = forms.ModelChoiceField(
        queryset=Materiais.objects.all().order_by('nome'), widget=forms.Select)
    umMaterial = forms.CharField(max_length=10)
    qtdMaterial = forms.DecimalField(max_digits=15, decimal_places=2)
    statusCotacao = forms.CharField(max_length=10)
    motivoReprovacao = forms.CharField(max_length=200)
    nomCliente = forms.ModelChoiceField(
        queryset=Clientes.objects.all().order_by('nome'), widget=forms.Select)

    # Associa formulario ao modelo
    class Meta:
        model = Cotacoes
        exclude = ()
