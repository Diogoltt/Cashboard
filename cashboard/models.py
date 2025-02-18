from django.db import models

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.email}"

class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.valor}"

class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.valor}"