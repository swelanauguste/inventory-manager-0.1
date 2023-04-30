# Generated by Django 4.1.7 on 2023-04-26 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0008_alter_printer_supplier"),
        ("assignments", "0012_alter_printerassignment_employee_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="printerassignment",
            name="printer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="printer_assignments",
                to="equipment.printer",
            ),
        ),
    ]