# Generated by Django 5.0.6 on 2024-05-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Nuevo_Cliente",
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
                    models.CharField(
                        db_column=" Nombre Cliente",
                        max_length=50,
                        verbose_name="Nombre Cliente",
                    ),
                ),
                (
                    "Nombre2",
                    models.CharField(
                        blank=True,
                        db_column="Segundo Nombre Cliente",
                        max_length=50,
                        verbose_name="Segundo Nombre Cliente",
                    ),
                ),
                (
                    "Apellido",
                    models.CharField(
                        db_column="Apellido", max_length=50, verbose_name="Apellido"
                    ),
                ),
                (
                    "Apellido2",
                    models.CharField(
                        blank=True,
                        db_column="Segundo Apellido",
                        max_length=50,
                        verbose_name="Segundo Apellido",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
                "db_table": "Nuevo_Cliente",
                "ordering": ["Apellido"],
            },
        ),
    ]
