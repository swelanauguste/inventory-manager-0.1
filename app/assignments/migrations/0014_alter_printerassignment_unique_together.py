# Generated by Django 4.1.7 on 2023-04-26 08:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("employees", "0004_rename_department_section_remove_employee_dept_and_more"),
        ("equipment", "0008_alter_printer_supplier"),
        ("assignments", "0013_alter_printerassignment_printer"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="printerassignment",
            unique_together={("employee", "printer")},
        ),
    ]
