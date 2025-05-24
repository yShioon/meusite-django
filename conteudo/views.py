from django.shortcuts import render, get_object_or_404
from .models import Postagem, Categoria

def home(request):
    posts = Postagem.objects.all().order_by('-criado_em')
    return render(request, 'home.html', {
        'posts': posts,
        'meta_title': 'Meu Site - Conteúdo de Qualidade',
        'meta_description': 'Encontre os melhores artigos sobre diversos temas'
    })

def detalhe_postagem(request, slug):
    post = get_object_or_404(Postagem, slug=slug)
    posts_relacionados = Postagem.objects.filter(
        categoria=post.categoria
    ).exclude(id=post.id)[:3]
    
    return render(request, 'detalhe.html', {
        'post': post,
        'posts_relacionados': posts_relacionados,
        'meta_title': post.titulo,
        'meta_description': post.resumo
    })

def posts_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    posts = Postagem.objects.filter(categoria=categoria)
    return render(request, 'home.html', {
        'posts': posts,
        'categoria': categoria,
        'meta_title': f'Posts sobre {categoria.nome}',
        'meta_description': f'Artigos sobre {categoria.nome}'
    })