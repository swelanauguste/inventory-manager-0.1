# Generated by Django 4.1.7 on 2023-04-11 16:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0008_alter_receiveitem_item_alter_removeitem_item"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="removeitem",
            name="price",
        ),
    ]
