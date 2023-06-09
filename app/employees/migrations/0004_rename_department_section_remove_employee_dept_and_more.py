# Generated by Django 4.1.7 on 2023-04-25 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0009_rename_dept_computerassignment_section_and_more"),
        ("stock", "0020_rename_dept_changeitem_section_and_more"),
        ("employees", "0003_unitsection_employee_unit"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Department",
            new_name="Section",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="dept",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="unit",
        ),
        migrations.AddField(
            model_name="employee",
            name="section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="employees.section",
                verbose_name="Section",
            ),
        ),
        migrations.DeleteModel(
            name="UnitSection",
        ),
    ]
