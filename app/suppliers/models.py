from django.db import models
from django.urls import reverse


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200, null=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("supplier-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

