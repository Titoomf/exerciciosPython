from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)  # argumente que voce deseja pasar e salva no banco
    slug = models.SlugField(max_length=255,
                            unique=True)  # endereco que aparece na pesquisa www.meusite/blo/introcao-ao-django
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()  # aqui eu deixo o usuario escrever o tamanho que ele quiser
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
