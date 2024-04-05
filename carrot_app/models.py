from django.db import models
from django.contrib.auth.models import User



class Tortas(models.Model):
    nombre = models.CharField(max_length=40)
    porciones = models.IntegerField(max_length=3)


    def __str__(self):
        return f'{self.nombre}'

class Catering(models.Model):
    evento = models.CharField(max_length=40)
    presupuesto = models.IntegerField()
    pax = models.IntegerField()

    def __str__(self):
        return f'{self.evento}'

class Pasteleria(models.Model):
    producto = models.CharField(max_length=40)
    tamaño = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.producto}, {self.tamaño}'

class Capacitaciones(models.Model):
    nombre = models.CharField(max_length=40)
    aula = models.CharField(max_length=40, default='Aula 505')

    def __str__(self):
        return f'{self.nombre}, {self.aula}'
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to='avatares')   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 