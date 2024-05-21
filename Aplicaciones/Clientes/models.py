from django.db import models

# Create your models here.
class Nuevo_Cliente(models.Model):
    Nombre = models.CharField(db_column=' Nombre Cliente', max_length=50, null=False,verbose_name='Nombre Cliente')    
    Nombre2 = models.CharField(db_column='Segundo Nombre Cliente', max_length=50, null=False,blank=True,verbose_name='Segundo Nombre Cliente')
    Apellido = models.CharField(db_column='Apellido', max_length=50, null=False,verbose_name='Apellido')
    Apellido2 = models.CharField(db_column='Segundo Apellido', max_length=50, null=False,blank=True,verbose_name='Segundo Apellido')
    #Telefono =models.IntegerField(db_column='Telefono',max_length=50,blank=True,verbose_name='Telefono')


    def __str__(self):
        return self.Nombre
    
    class Meta:
        ordering =['Apellido']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Nuevo_Cliente'
        app_label = 'Clientes'
