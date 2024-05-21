# Generated by Django 5.0.6 on 2024-05-18 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Departamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Nombre",
                    models.CharField(db_column="Nombre Departamento", max_length=50),
                ),
            ],
            options={
                "verbose_name": "Departamento",
                "verbose_name_plural": "Departamentos",
                "db_table": "Departamento",
                "ordering": ["Nombre"],
            },
        ),
        migrations.CreateModel(
            name="Ciudad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Nombre", models.CharField(db_column="Nombre Ciudad", max_length=50)),
                (
                    "id_departamento",
                    models.ForeignKey(
                        db_column="Codigo Departamento",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="Consultas.departamento",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ciudad",
                "verbose_name_plural": "Ciudades",
                "db_table": "Ciudad",
                "ordering": ["Nombre"],
            },
        ),
    ]
