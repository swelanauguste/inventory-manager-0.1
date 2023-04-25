# Generated by Django 4.1.7 on 2023-04-13 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0003_unitsection_employee_unit"),
        ("stock", "0013_alter_changeitem_options"),
        ("assignments", "0002_alter_computerassignment_date_assigned_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItemAssignment",
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
                ("date_assigned", models.DateField(auto_now_add=True)),
                ("date_returned", models.DateField(blank=True, null=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="employees.employee",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="stock.item",
                    ),
                ),
            ],
        ),
    ]