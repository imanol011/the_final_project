# Generated by Django 4.1.5 on 2023-01-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='products', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]