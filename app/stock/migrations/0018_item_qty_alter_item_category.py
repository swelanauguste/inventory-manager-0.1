# Generated by Django 4.1.7 on 2023-04-19 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("stock", "0017_remove_item_category_item_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="qty",
            field=models.IntegerField(default=0, verbose_name="quantity"),
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="stock.category",
            ),
        ),
    ]
