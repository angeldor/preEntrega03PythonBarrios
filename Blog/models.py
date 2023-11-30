from django.db import models

# Create your models here.
class Author(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __srt__(self):
        return f"{self.nombre} {self.apellido}"
    
class Blog(Author):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()

    def __str__(self):
        return f"{self.titulo} por {self.nombre} {self.apellido}"
    
class Category(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre