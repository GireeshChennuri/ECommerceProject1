from ...models import *
from  user.models import *
# from products.models import *
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    help = 'Populates the database with realistic product names under proper categories'

    def handle(self, *args, **kwargs):
        user=User.objects.get(id=5)
        order=Order.objects.all()
        # item=OrderItem.objects.get(order=order,product__id=22)
        # item.quantity=3
        # item.save()
        # # item.delete()
        # # orders=Order.objects.filter(user=user)
        # # r1=OrderItem.objects.get(id=1)
        # print(item)
        # print(order.items.all())
        order=Order.objects.filter(user=user)
        ord=order[0]
        item=OrderItem.objects.get(order=ord,product__id=22)
        item.quantity=2
        item.save()
        print(item.item_subtotal)
        # ord.save()
        print(item.order.total_price)
        # for ord in order:
        #     # ord.total_price=0
        #     ord.update_total_price()
         