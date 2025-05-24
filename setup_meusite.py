import os

files = {
    "manage.py": """#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meusite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
""",
    "requirements.txt": "Django>=4.2\n",
    "meusite/__init__.py": "",
    "meusite/settings.py": """import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-minha-chave-secreta-1234567890'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'conteudo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meusite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'meusite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
""",
    "meusite/urls.py": """from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('conteudo.urls')),
]
""",
    "meusite/wsgi.py": """import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meusite.settings')
application = get_wsgi_application()
""",
    "conteudo/__init__.py": "",
    "conteudo/apps.py": """from django.apps import AppConfig

class ConteudoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'conteudo'
    verbose_name = "Conteúdo"
""",
    "conteudo/models.py": """from django.db import models

class Postagem(models.Model):
    titulo = models.CharField('Título', max_length=200)
    conteudo = models.TextField('Conteúdo')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
""",
    "conteudo/admin.py": """from django.contrib import admin
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criado_em')
    search_fields = ('titulo',)
    list_filter = ('criado_em',)
""",
    "conteudo/views.py": """from django.shortcuts import render, get_object_or_404
from .models import Postagem

def home(request):
    posts = Postagem.objects.all()
    return render(request, 'home.html', {'posts': posts})

def detalhe_postagem(request, postagem_id):
    post = get_object_or_404(Postagem, id=postagem_id)
    return render(request, 'detalhe.html', {'post': post})
""",
    "conteudo/urls.py": """from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:postagem_id>/', views.detalhe_postagem, name='detalhe_postagem'),
]
""",
    "templates/home.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Meu Site de Conteúdo</title>
    <!-- Google Adsense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3625069878363794"
        crossorigin="anonymous"></script>
</head>
<body>
    <h1>Últimas Postagens</h1>
    {% for post in posts %}
        <h2><a href="{% url 'detalhe_postagem' post.id %}">{{ post.titulo }}</a></h2>
        <p>{{ post.criado_em|date:"d/m/Y H:i" }}</p>
        <hr>
    {% empty %}
        <p>Nenhuma postagem ainda.</p>
    {% endfor %}

    <!-- Bloco de anúncio Adsense -->
    <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-3625069878363794"
        data-ad-slot=""
        data-ad-format="auto"></ins>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</body>
</html>
""",
    "templates/detalhe.html": """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>{{ post.titulo }}</title>
    <!-- Google Adsense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-3625069878363794"
        crossorigin="anonymous"></script>
</head>
<body>
    <h1>{{ post.titulo }}</h1>
    <p>{{ post.criado_em|date:"d/m/Y H:i" }}</p>
    <div>{{ post.conteudo|linebreaks }}</div>

    <!-- Bloco de anúncio Adsense -->
    <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-3625069878363794"
        data-ad-slot=""
        data-ad-format="auto"></ins>
    <script>
        (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</body>
</html>
""",
}

folders = [
    "meusite",
    "conteudo",
    "templates"
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Estrutura do projeto Django criada! Siga as instruções para instalar e rodar.")