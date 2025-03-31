# Generated by Django 4.2.7 on 2023-11-21 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0005_rename_definicion_definicions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conceptos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.TextField(max_length=50)),
                ('def_inicial', models.TextField(max_length=200)),
                ('def_solucion', models.TextField(max_length=300)),
                ('nota', models.TextField(max_length=300)),
                ('ParteLeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.parteleccion')),
            ],
        ),
        migrations.DeleteModel(
            name='Definicions',
        ),
    ]
