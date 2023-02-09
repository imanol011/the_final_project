# Generated by Django 4.1.5 on 2023-01-31 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.AddField(
            model_name='products',
            name='products_image',
            field=models.ImageField(blank=True, null=True, upload_to='products_image', verbose_name='Imagen'),
        ),
    ]
