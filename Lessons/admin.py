from django.contrib import admin
from .models import Leccion, ParteLeccion, Historia, Ejercicio, ExamenDGT, Concepto

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion',)

@admin.register(ParteLeccion)
class ParteLeccionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'leccion', 'descripcion',)

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'parte_leccion',)


@admin.register(Concepto)
class ConceptoAdmin(admin.ModelAdmin):
    list_display = ('clave', 'def_inicial','def_solucion','nota')



@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'parte_leccion')

@admin.register(ExamenDGT)
class ExamenDGTAdmin(admin.ModelAdmin):
    list_display = ('leccion',)
