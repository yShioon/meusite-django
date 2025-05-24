from django.db import models

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
