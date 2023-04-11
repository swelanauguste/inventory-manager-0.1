from django.conf import settings
from django.db import models
from django.urls import reverse
from suppliers.models import Supplier

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, blank=True, related_name="items")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["name"]

    @property
    def get_total_item_qty(self):
        return sum(item.qty for item in self.items.all())

    @property
    def get_total_cost(self):
        return self.get_total_count() * self.price

    def get_total_count(self):
        return sum(item.qty for item in self.items.all() if item.qty > 0)

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class ChangeItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items")
    qty = models.IntegerField("quantity")
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.item} ({self.qty})"
