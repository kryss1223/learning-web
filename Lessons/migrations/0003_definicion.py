# Generated by Django 4.2.3 on 2023-11-16 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0002_leccion_descripcion_parteleccion_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.IntegerField()),
                ('definicion', models.TextField()),
                ('nota', models.TextField(blank=True, null=True)),
                ('parte_leccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.parteleccion')),
            ],
        ),
    ]
