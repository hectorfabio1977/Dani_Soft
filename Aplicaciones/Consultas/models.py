from django.db import models

# Create your models here.
class Departamento(models.Model):
    Nombre =models.CharField(db_column='Nombre Departamento',max_length=50, null=False)

    def __str__(self):
        return self.Nombre
    
    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        db_table = 'Departamento'
        app_label = 'Consultas'

class Ciudad(models.Model):
    Nombre = models.CharField(db_column='Nombre Ciudad', max_length=50, null=False)
    id_departamento =models.ForeignKey('Departamento',db_column='Codigo Departamento',null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.Nombre
    
    class Meta:
        ordering = ['Nombre']
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'Ciudad'
        app_label = 'Consultas'
