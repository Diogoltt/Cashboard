from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def mercado(request):
    return render(request, 'mercado.html')
def pet(request):
    return render(request, 'pet.html')
def dashboard(request):
    return render(request, 'dashboard.html')