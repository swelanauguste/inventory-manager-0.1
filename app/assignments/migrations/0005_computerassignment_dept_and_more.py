# Generated by Django 4.1.7 on 2023-04-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0003_unitsection_employee_unit"),
        ("assignments", "0004_delete_itemassignment"),
    ]

    operations = [
        migrations.AddField(
            model_name="computerassignment",
            name="dept",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.department",
            ),
        ),
        migrations.AddField(
            model_name="computerassignment",
            name="unit_section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.unitsection",
            ),
        ),
        migrations.AddField(
            model_name="printerassignment",
            name="dept",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.department",
            ),
        ),
        migrations.AddField(
            model_name="printerassignment",
            name="unit_section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.unitsection",
            ),
        ),
        migrations.AddField(
            model_name="scannerassignment",
            name="dept",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.department",
            ),
        ),
        migrations.AddField(
            model_name="scannerassignment",
            name="unit_section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.unitsection",
            ),
        ),
    ]
