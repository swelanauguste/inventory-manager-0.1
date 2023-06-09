# Generated by Django 4.1.7 on 2023-04-15 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0008_alter_printer_supplier"),
        ("employees", "0003_unitsection_employee_unit"),
        ("assignments", "0006_alter_printerassignment_employee"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printerassignment",
            name="dept",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computer_assignments",
                to="employees.department",
            ),
        ),
        migrations.AlterField(
            model_name="printerassignment",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="printer_assignments",
                to="employees.employee",
            ),
        ),
        migrations.AlterField(
            model_name="printerassignment",
            name="printer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computer_assignments",
                to="equipment.printer",
            ),
        ),
        migrations.AlterField(
            model_name="printerassignment",
            name="unit_section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="computer_assignments",
                to="employees.unitsection",
            ),
        ),
    ]
