from django.db import models


class Cliente(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=200)
    data_registro = models.DateTimeField('data de registro')
    endereco = models.CharField(max_length=200)
    genero = models.CharField(max_length=2, choices=GENEROS)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Mesa(models.Model):
    preco_hora = models.IntegerField(default=20)
    titulo = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente)
    mesa = models.ForeignKey(Mesa)
    data_reserva = models.DateTimeField('data de registro da reserva')
    data_jogo = models.DateTimeField('data de uso da mesa')

    def __str__(self):
        return '{} - {}'.format(self.cliente, self.mesa)

