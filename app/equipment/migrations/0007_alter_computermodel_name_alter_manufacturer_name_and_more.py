# Generated by Django 4.1.7 on 2023-04-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0006_rename_printerremarks_printerremark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="computermodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="manufacturer",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="monitormodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="printermodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="scannermodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
