from django.db import models

class Operacion(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    resul = models.IntegerField()
    operacion = models.CharField(max_length=10)
