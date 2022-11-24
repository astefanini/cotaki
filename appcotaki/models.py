from django.db import models

# Create your models here.


class Materiais(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    nome = models.CharField(max_length=200)
    um = models.CharField(max_length=10)
    precoUnit = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['codigo'], name='materiais_unique')
        ]


class Fabricantes(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    nome = models.CharField(max_length=200)
    produto = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['codigo'], name='fabricantes_unique')
        ]


class Clientes(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    nome = models.CharField(max_length=200)


class Comissoes(models.Model):
    codigo = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Codigo')
    percentual = models.DecimalField(max_digits=15, decimal_places=2)


class Pedidos(models.Model):
    numPedido = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Numero')
    data = models.DateField()
    nomeFabricante = models.CharField(max_length=200)
    tipoMaterial = models.CharField(max_length=200)
    umMaterial = models.CharField(max_length=10)
    qtdMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    precoUnitMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    precoTotalMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    statusPedido = (
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
        ('E', 'Em análise'),
    )
    motivoReprovacao = models.CharField(max_length=200)
    numCotacao = models.IntegerField()
    nomCliente = models.CharField(max_length=200)
    percComissao = models.DecimalField(max_digits=15, decimal_places=2)
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
                fields=['numPedido'], name='pedidos_unique')
        ]


class Cotacoes(models.Model):
    numCotacao = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='Numero')
    data = models.DateField()
    nomeFabricante = models.CharField(max_length=200)
    tipoMaterial = models.CharField(max_length=200)
    umMaterial = models.CharField(max_length=10)
    qtdMaterial = models.DecimalField(max_digits=15, decimal_places=2)
    statusCotacao = (
        ('A', 'Aprovado'),
        ('R', 'Reprovado'),
        ('E', 'Em análise'),
    )
    motivoReprovacao = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['numCotacao'], name='cotacoes_unique')
        ]
