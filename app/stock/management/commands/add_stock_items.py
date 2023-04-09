from decimal import Decimal
from random import randint

from django.core.management.base import BaseCommand
from faker import Faker
from suppliers.models import Supplier

from ...models import Category, Item


class Command(BaseCommand):
    help = "Add faker data to the database"

    def handle(self, *args, **kwargs):
         # f_cat = Category.objects.earliest("pk").pk
        # l_cat = Category.objects.latest("pk").pk
        f_sup = Supplier.objects.earliest("pk").pk
        l_sup = Supplier.objects.latest("pk").pk
        fake = Faker()
        for _ in range(50):
            name = fake.name_nonbinary()
            # category_list = Category.objects.get(pk=randint(f_cat, l_cat))
            supplier = Supplier.objects.get(pk=randint(f_sup, l_sup))
            quantity = randint(5, 49)
            price = Decimal(randint(5, 49))
            # print(name, category, supplier, price, quantity)
            Item.objects.get_or_create(
                name=name,
                # category=Category.add(category_list),
                supplier=supplier,
                quantity=quantity,
                price=price
            )
            self.stdout.write(self.style.SUCCESS(f"{name}"))
