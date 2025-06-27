import random
import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Product
from orders.models import Order, OrderItem
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = "Populate random orders with order items"

    def handle(self, *args, **kwargs):
        users = list(User.objects.all())
        products = list(Product.objects.all())

        if not users or not products:
            self.stdout.write(self.style.ERROR("Users or Products not found. Add them first."))
            return

        for _ in range(10):  # create 10 orders
            user = random.choice(users)
            order = Order.objects.create(user=user, status=random.choice(Order.StatusChoices.values))
            
            selected_products = random.sample(products, k=random.randint(1, 5))  # choose 1-5 random products
            for product in selected_products:
                quantity = random.randint(1, 3)
                OrderItem.objects.create(order=order, product=product, quantity=quantity)

            self.stdout.write(self.style.SUCCESS(f"Created order {order.order_id} for {user.username}"))

        self.stdout.write(self.style.SUCCESS("✅ Successfully populated random orders"))
