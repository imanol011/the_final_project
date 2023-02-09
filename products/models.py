from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    price = models.FloatField(verbose_name='Precio')
    stock = models.BooleanField(default=True, verbose_name='En Stock')
    products_image = models.ImageField(upload_to='products_image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


