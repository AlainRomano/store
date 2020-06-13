from django.shortcuts import render, redirect
# from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {
        'message': 'hello world from sight',
        'title': 'Products',
        'products': [
            {'title': 'Remera', 'price': 50, 'stock': True},
            {'title': 'Bermuda', 'price': 120, 'stock': True},
            {'title': 'Pantalon', 'price': 70, 'stock': True},
            {'title': 'Buzo', 'price': 299, 'stock': False},
            {'title': 'Laptop', 'price': 1234, 'stock': True}
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña incorrectos')
    return render(request, 'users/login.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')