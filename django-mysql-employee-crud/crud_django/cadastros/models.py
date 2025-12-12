from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique= True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome