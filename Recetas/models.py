from django.db import models

class MundoRecetas(models.Model):
    nombre = models.CharField(max_length=50)
    grupo = models.CharField(max_length=100)
    receta = models.CharField(max_length=100)
    detalle = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now=True)


    def __str__(self):
        return (f'{self.nombre} {self.grupo} {self.receta} {self.detalle} ')
    

    