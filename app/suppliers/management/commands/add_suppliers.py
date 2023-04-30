from django.core.management.base import BaseCommand

from ...models import Supplier


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
        Supplier.objects.get_or_create(
            name='kingship',
            address='Derriere Fort, the Morne,',
            address1='CASTRIES',
            phone="758-489-3909",
            email='kingship.lc@gmail.com',
        )
        self.stdout.write(self.style.SUCCESS("kingship"))
