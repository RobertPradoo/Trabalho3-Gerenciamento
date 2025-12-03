# Create your models here.
from django.db import models


class Carro(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100)

    class Meta:
        db_table = "carro"
        verbose_name = "Carro"
        verbose_name_plural = "Carros"


class Piloto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cor_capacete = models.CharField(max_length=50)
    podios = models.IntegerField(default=0)
    vitorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)

    class Meta:
        db_table = "piloto"
        verbose_name = "Piloto"
        verbose_name_plural = "Pilotos"


class Corrida(models.Model):
    id = models.AutoField(primary_key=True)
    local = models.CharField(max_length=100)
    data = models.DateField()
    tamanho_grid = models.IntegerField(
        help_text="Número máximo de inscrições permitidas para a corrida."
    )
    safety_car = models.BooleanField(default=False)
    count_batidas = models.IntegerField(default=0)
    campeonato = models.ForeignKey(
        "Campeonato", on_delete=models.CASCADE, related_name="corridas"
    )

    class Meta:
        db_table = "corrida"
        verbose_name = "Corrida"
        verbose_name_plural = "Corridas"


class InscricaoCorrida(models.Model):
    id = models.AutoField(primary_key=True)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    data_inscricao = models.DateField(auto_now_add=True)
    posicao_largada = models.IntegerField(null=True, blank=True)
    posicao_chegada = models.IntegerField(null=True, blank=True)
    tempo_corrida = models.DurationField(null=True, blank=True)
    corrida = models.ForeignKey(
        Corrida, on_delete=models.CASCADE, related_name="inscricoes"
    )

    class Meta:
        db_table = "inscricao_corrida"
        verbose_name = "Inscrição Corrida"
        verbose_name_plural = "Inscrições Corrida"


class Campeonato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()

    class Meta:
        db_table = "campeonato"
        verbose_name = "Campeonato"
        verbose_name_plural = "Campeonatos"
