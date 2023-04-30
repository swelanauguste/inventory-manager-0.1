from django.core.management.base import BaseCommand

from assignments.models import ComputerAssignment

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        ComputerAssignment.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Deleted"))