# Generated by Django 4.1.7 on 2023-05-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("equipment", "0010_remove_printermodel_ink_printermodel_ink"),
    ]

    operations = [
        migrations.AddField(
            model_name="computer",
            name="is_assigned",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="printer",
            name="is_assigned",
            field=models.BooleanField(default=False),
        ),
    ]
