import csv

from django.core.management.base import BaseCommand

from ...models import Item, Category

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        
        with open(f"static/csv/inks_cleaned.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for i, row in enumerate(reader):
                name = row[0].replace("\n", "")
                init_count = int(row[1])
                category = Category.objects.get(name__icontains='ink')
                Item.objects.get_or_create(
                    name=name,
                    init_count=init_count,
                    category=category
                )
                self.stdout.write(self.style.SUCCESS(f"{name} {init_count} {category} added"))
                
            