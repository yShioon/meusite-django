from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:postagem_id>/', views.detalhe_postagem, name='detalhe_postagem'),
]
