from django.db import models
from django.utils import timezone


class PostManager(models.Manager):

    def posts_ordenados_por_publicacion(self):
        resultado = self.filter(
            published_date__lte=timezone.now()).order_by('-published_date')
        return resultado
