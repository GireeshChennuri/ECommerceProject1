from ...models import Category, Product
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Populates the database with realistic product names under proper categories'

    def handle(self, *args, **kwargs):
        c=Category.objects.get(id=6)
        print(c.products.all())
        print()