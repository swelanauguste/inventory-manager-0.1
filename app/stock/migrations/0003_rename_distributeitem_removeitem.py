# Generated by Django 4.1.7 on 2023-04-08 10:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stock", "0002_rename_giveitem_distributeitem"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DistributeItem",
            new_name="RemoveItem",
        ),
    ]
