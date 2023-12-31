# Generated by Django 4.2.3 on 2023-09-12 06:27

import aboutme.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMePerfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('image', models.ImageField(upload_to=aboutme.models.custom_upload_to, verbose_name='Portada')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fechade creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Perfil',
                'ordering': ['-created'],
            },
        ),
    ]
