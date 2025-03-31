# models.py
from django.db import models
import random
# Creamos las lecciones y su contenido
class Leccion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=150, default="Descripción predeterminada") # Al añadir nuevos datos se debe de poner un default

class ParteLeccion(models.Model):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, default="Descripción predeterminada")

class Historia(models.Model):
    parte_leccion = models.ForeignKey(ParteLeccion, on_delete=models.CASCADE)
    contenido = models.TextField()

class Ejercicio(models.Model):
    parte_leccion = models.ForeignKey(ParteLeccion, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    datos_especificos = models.JSONField()
    partes_leccion_validas = models.ManyToManyField(ParteLeccion, related_name='ejercicios_validos')

class Concepto(models.Model):
    ParteLeccion = models.ForeignKey(ParteLeccion, on_delete=models.CASCADE)
    tipos_ejercicio_validos = models.ManyToManyField(Ejercicio)
    clave = models.TextField(max_length=50)
    def_inicial = models.TextField(max_length=200)
    def_solucion = models.TextField(max_length=300)
    nota = models.TextField(max_length=300, default= 'no hay nota')
    
class ExamenDGT(models.Model):
    leccion = models.ForeignKey(ParteLeccion, on_delete=models.CASCADE)
    preguntas = models.ManyToManyField(Ejercicio)
