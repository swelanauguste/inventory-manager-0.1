# Generated by Django 4.1.7 on 2023-04-09 11:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0004_alter_item_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["name"]},
        ),
    ]
