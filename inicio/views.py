from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from colaboradores.models import Colaborador


@login_required()
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'inicio/index.html', data)
