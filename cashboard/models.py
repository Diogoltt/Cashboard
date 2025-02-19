from django.db import models
from django.contrib.auth.models import User

class Despesa(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="despesa", default=1)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.valor}"

class Receita(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receita", default=1)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=255)
    data = models.DateField()

    def __str__(self):
        return f"{self.descricao} - {self.valor}"