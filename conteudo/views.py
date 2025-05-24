from django.shortcuts import render, get_object_or_404
from .models import Postagem

def home(request):
    posts = Postagem.objects.all()
    return render(request, 'home.html', {'posts': posts})

def detalhe_postagem(request, postagem_id):
    post = get_object_or_404(Postagem, id=postagem_id)
    return render(request, 'detalhe.html', {'post': post})
