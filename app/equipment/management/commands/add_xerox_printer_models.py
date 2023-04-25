import csv
from random import randint
from django.core.management.base import BaseCommand

from ...models import PrinterModel, Manufacturer

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/xerox_printers_cleaned.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name = row[0].replace("\n", "").lower()
                manufacturer = Manufacturer.objects.get(name__icontains='xerox')
                colour_printer = randint(0, 1)
                PrinterModel.objects.get_or_create(
                    name=name,
                    manufacturer=manufacturer,
                    colour_printer=colour_printer
                )
                self.stdout.write(self.style.SUCCESS(f"{name} {manufacturer} {colour_printer} added"))
                
            