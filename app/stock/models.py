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
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.IntegerField(default=1, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    
    class Meta:
        ordering = ['name']

    def get_total_cost(self):
        return self.price * self.get_item_total_count()

    def get_all_received_count(self):
        return sum(item.qty for item in self.receive_items.all())

    def get_all_given_count(self):
        return sum(item.qty for item in self.give_items.all())

    def get_item_total_count(self):
        return (
            self.get_all_received_count() + self.quantity
        ) - self.get_all_given_count()

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class ReceiveItem(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="receive_items"
    )
    qty = models.PositiveIntegerField("quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.item} ({self.qty})"


class RemoveItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="give_items")
    qty = models.PositiveIntegerField("quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.item} ({self.qty})"
