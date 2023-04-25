from django.conf import settings
from django.db import models
from django.urls import reverse
from employees.models import Department, Employee, UnitSection
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
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories", null=True, blank=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    init_count = models.IntegerField("quantity", default=1)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        ordering = ["name"]

    @property
    def get_total_item_balance(self):
        return sum(item.qty for item in self.items.all()) + self.init_count

    @property
    def get_total_cost(self):
        return self.get_item_qty_of_all_time() * self.price

    def get_item_qty_of_all_time(self):
        return (
            sum(item.qty for item in self.items.all() if item.qty > 0) + self.init_count
        )

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})


    def __str__(self):
        return self.name


class ChangeItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="items")
    qty = models.IntegerField("quantity")
    dept = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True
    )
    unit_section = models.ForeignKey(
        UnitSection, on_delete=models.CASCADE, null=True, blank=True
    )
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, null=True, blank=True
    )
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="+"
    )

    class Meta:
        ordering = ("-created_at",)

    # def get_absolute_url(self):
    #     return reverse("item-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.item} ({self.qty})"
