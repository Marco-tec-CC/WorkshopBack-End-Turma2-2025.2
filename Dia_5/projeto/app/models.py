from django.db import models

# Create your models here.
class ViaCep(models.Model):
    rua = models.CharField(max_length=225)
    bairro = models.CharField(max_length=225)
    cidade = models.CharField(max_length=225)
    estado = models.CharField(max_length=225)
    cep = models.CharField(max_length=225)

    def __str__(self):
        return f"rua: {self.rua}, Bairro: {self.bairro}, cidade: {self.cidade}, Estado: {self.estado}, CEP: {self.cep}"