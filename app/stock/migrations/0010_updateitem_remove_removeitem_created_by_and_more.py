# Generated by Django 4.1.7 on 2023-04-11 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("stock", "0009_remove_removeitem_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="UpdateItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qty", models.PositiveIntegerField(verbose_name="quantity")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="removeitem",
            name="created_by",
        ),
        migrations.RemoveField(
            model_name="removeitem",
            name="item",
        ),
        migrations.RemoveField(
            model_name="removeitem",
            name="updated_by",
        ),
        migrations.AddField(
            model_name="item",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0, max_digits=10
            ),
        ),
        migrations.DeleteModel(
            name="ReceiveItem",
        ),
        migrations.DeleteModel(
            name="RemoveItem",
        ),
        migrations.AddField(
            model_name="updateitem",
            name="item",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_items",
                to="stock.item",
            ),
        ),
        migrations.AddField(
            model_name="updateitem",
            name="updated_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
