# Generated by Django 4.1.5 on 2023-02-01 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='condition',
            field=models.CharField(choices=[('Nacional', 'Nacional'), ('Internacional', 'Internacional'), ('Independiente', 'Independiente')], max_length=50),
        ),
    ]