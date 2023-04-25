import csv

from django.core.management.base import BaseCommand

from ...models import ChangeItem, Item



ChangeItem.objects.all().delete()
Item.objects.all().delete()

class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        ChangeItem.objects.all().delete()
        Item.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Delete"))
