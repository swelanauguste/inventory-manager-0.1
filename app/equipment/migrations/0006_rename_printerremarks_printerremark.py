# Generated by Django 4.1.7 on 2023-04-15 11:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("equipment", "0005_printermodel_ink_printerremarks"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PrinterRemarks",
            new_name="PrinterRemark",
        ),
    ]
