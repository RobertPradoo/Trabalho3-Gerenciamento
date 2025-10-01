# Create your models here.
from django.db import models


class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = "carro"
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
