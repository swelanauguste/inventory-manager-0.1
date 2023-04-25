from django.core.management.base import BaseCommand

from ...models import Section


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(f"static/docs/section_list.txt") as file:
            for row in file:
                name = row.replace("\n", "").lower()
                Section.objects.get_or_create(
                    name=name,
                )
                self.stdout.write(self.style.SUCCESS(f"{name} added"))