import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from products.models.product.categories import Category
from products.models.product.products import Product

fake = Faker()


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument(
            "count",
            type=int,
            nargs="?",
            default=50,
            help="Number of products to generate"
        )

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        categories = list(Category.objects.all())
        users = list(User.objects.all())

        if not categories or not users:
            self.stdout.write(self.style.ERROR("Error: No categories or users found!"))
            return

        for _ in range(count):
            Product.objects.create(
                title=fake.sentence(nb_words=3),
                price=round(random.uniform(10, 500), 2),
                quantity=random.randint(1, 50),
                category=random.choice(categories),
                seller=random.choice(users),
                short_description=fake.text(max_nb_chars=100),
                long_description=fake.text(max_nb_chars=500)
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully added {count} fake products!"))
