from django.db import models
import uuid
# Create your models here.

class Empleado (models.Model):

    dni_choices = (
        ('nit', 'NIT'),
        ('cc', 'Cédula de Ciudadanía'),
    )
    id_empleado = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    tipo_identificacion = models.CharField(max_length = 3, choices = dni_choices) 
    identificacion = models.CharField(max_length = 20)
    fecha_ingreso = models.DateField()
    salario_mensual = models.DecimalField(max_digits = 10, decimal_places = 2)
    cargo = models.CharField(max_length = 100)
    departamento = models.CharField(max_length = 100)

    class Meta:
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['nombre']

class Telefono(models.Model):
    cel_choices = (
        ('cell', 'Celular'),
        ('tel', 'Teléfono'),
    )
    tel_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    tipo = models.CharField(max_length = 4, choices = cel_choices)
    numero = models.CharField(max_length = 15)
    indicativo = models.CharField(max_length = 5)
    empleado = models.ForeignKey(Empleado, related_name = 'telefonos', on_delete = models.CASCADE)

    class Meta:
        db_table = 'telefono'
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        ordering = ['numero']

class Email(models.Model):
    email_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    email = models.EmailField()
    empleado = models.ForeignKey(Empleado, related_name='emails', on_delete=models.CASCADE)

    class Meta:
        db_table = 'email'
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ['email']