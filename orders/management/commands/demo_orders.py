from ...models import *
# from  user.models import *
# from products.models import *
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Populates the database with realistic product names under proper categories'

    def handle(self, *args, **kwargs):
        c=Order.objects.filter(user__id=1)
        # r1=OrderItem.objects.get(id=1)
        print(len(c[0].items.all()))