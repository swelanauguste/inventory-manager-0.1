from django.db import models
from django.urls import reverse


class Section(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("section-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name.title()


class Employee(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Section",
    )
    ext = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name.title()
