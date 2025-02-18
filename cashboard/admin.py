from django.contrib import admin
from .models import Despesa, Receita, Usuario

# Register your models here.
admin.site.register(Receita)
admin.site.register(Despesa)
admin.site.register(Usuario)