from django.contrib import admin
from .models import Despesa, Receita

# Register your models here.
admin.site.register(Receita)
admin.site.register(Despesa)
