# Generated by Django 4.1.5 on 2023-02-08 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_products_products_picture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='products_image',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]