from django.core.management.base import BaseCommand

from ...models import ComputerModel, Manufacturer


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/hp_model_list.txt") as file:
            for row in file:
                name = row.replace("\n", "")
                manufacturer = Manufacturer.objects.get(name__icontains='hp')
                ComputerModel.objects.get_or_create(
                    name=name,
                    manufacturer=manufacturer
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))