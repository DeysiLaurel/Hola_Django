from django.db import models

#Create models
class Mensaje(models.Model):
    mensaje = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)


    def __str__(self):
        return self.mensaje