# Generated by Django 4.1.5 on 2023-02-08 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_products_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='products_image',
            field=models.ImageField(blank=True, null=True, upload_to='products_image'),
        ),
    ]
