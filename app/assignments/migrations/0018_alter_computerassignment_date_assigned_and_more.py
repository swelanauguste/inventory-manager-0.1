# Generated by Django 4.1.7 on 2023-04-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0017_alter_computerassignment_date_assigned_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computerassignment",
            name="date_assigned",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="computerassignment",
            name="date_returned",
            field=models.DateField(blank=True, null=True),
        ),
    ]