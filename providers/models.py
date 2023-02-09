from django.db import models

class Provider(models.Model):
    CONDITION_CHOICES = (
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
        ('Independiente', 'Independiente'),
    )

    name = models.CharField(max_length=100, verbose_name='Nombre')
    address = models.CharField(max_length=300, verbose_name='Dirección')
    phone_number = models.CharField(max_length=20, verbose_name='Telefono')
    email = models.EmailField()
    record_company = models.CharField(max_length=50, choices = CONDITION_CHOICES, verbose_name='Discográfica')
    is_active = models.BooleanField(default=True, verbose_name='Activa')

    def __str__(self):
        return f'{self.name} - {self.email}'
