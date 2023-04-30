from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Supplier


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(50):
            name=fake.company()
            Supplier.objects.get_or_create(
                name='kingship',
                address='Derriere Fort, the Morne,',
                address1='CASTRIES',
                phone="758-489-3909",
                email='kingship.lc@gmail.com',
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
