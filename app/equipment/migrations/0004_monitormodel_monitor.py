# Generated by Django 4.1.7 on 2023-04-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("suppliers", "0001_initial"),
        ("equipment", "0003_alter_computermodel_memory_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="MonitorModel",
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
                ("name", models.CharField(max_length=255)),
                ("size", models.CharField(blank=True, default='22"', max_length=255)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="equipment.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Monitor",
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
                    "serial_number",
                    models.CharField(db_index=True, max_length=255, unique=True),
                ),
                (
                    "model",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="monitor",
                        to="equipment.monitormodel",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="monitors",
                        to="suppliers.supplier",
                    ),
                ),
            ],
        ),
    ]
