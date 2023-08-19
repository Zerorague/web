from django.db import models

# Create your models here.


class Aviso(models.Model):
    asunto = models.CharField(max_length=50)
    mensaje = models.CharField(max_length=500)
