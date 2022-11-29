from django.db import models

# Create your models here.


class Materiais(models.Model):
    nome = models.CharField(max_length=200, primary_key='true')
    um = models.CharField(max_length=10)
    precoUnit = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nome'], name='materiais_unique')
        ]


class Fabricantes(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo', default=1)
    nome = models.CharField(max_length=200)
    produto = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['codigo'], name='fabricantes_unique')
        ]


class Clientes(models.Model):
    nome = models.CharField(max_length=200, primary_key='true')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['nome'], name='clientes_unique')
        ]


class Comissoes(models.Model):
    percentual = models.DecimalField(
        max_digits=15, decimal_places=2, default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['percentual'], name='comissoes_unique')
        ]


class Cotacoes(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    numCotacao = models.IntegerField(default=0)
    data = models.DateField()
    nomeFabricante = models.ForeignKey(
        Fabricantes, related_name='fabricante', on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(
        Materiais, related_name='tipomateriais', on_delete=models.CASCADE)
    umMaterial = models.CharField(max_length=10)
    qtdMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    statusCotacao = models.CharField(max_length=10, default='Em análise')
    motivoReprovacao = models.CharField(max_length=200)
    nomCliente = models.ForeignKey(
        Clientes, related_name='cotacaoclientes', on_delete=models.CASCADE, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['codigo'], name='cotacoes_unique')
        ]


class Pedidos(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    numPedido = models.IntegerField(default=0)
    data = models.DateField()
    nomeFabricante = models.ForeignKey(
        Fabricantes, related_name='fabricantes', on_delete=models.CASCADE)
    tipoMaterial = models.ForeignKey(
        Materiais, related_name='materiais', on_delete=models.CASCADE)
    umMaterial = models.CharField(max_length=10)
    qtdMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    precoUnitMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    precoTotalMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    statusPedido = models.CharField(max_length=10, default='Em análise')
    motivoReprovacao = models.CharField(max_length=200)
    numCotacao = models.ForeignKey(
        Cotacoes, related_name='cotacoes', on_delete=models.CASCADE)
    nomCliente = models.ForeignKey(
        Clientes, related_name='clientes', on_delete=models.CASCADE)
    percComissao = models.ForeignKey(
        Comissoes, related_name='comissoes', on_delete=models.CASCADE)
    valorComissao = models.DecimalField(max_digits=15, decimal_places=2)
    valorA = models.DecimalField(max_digits=15, decimal_places=2)
    dataA30 = models.DateField()
    valorB = models.DecimalField(max_digits=15, decimal_places=2)
    dataB60 = models.DateField()
    valorC = models.DecimalField(max_digits=15, decimal_places=2)
    dataC90 = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['codigo'], name='pedidos_unique')
        ]
