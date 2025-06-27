from django.core.management.base import BaseCommand
from ...models import Category, Product
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Populates the database with realistic product names under proper categories'

    def handle(self, *args, **kwargs):
        category_product_map = {
            "Electronics": [
                "Smartphone", "Laptop", "Bluetooth Speaker", "Smartwatch", "Wireless Earbuds"
            ],
            "Groceries": [
                "Basmati Rice", "Olive Oil", "Whole Wheat Flour", "Green Tea", "Brown Sugar"
            ],
            "Clothing": [
                "Denim Jeans", "Cotton T-Shirt", "Formal Shirt", "Winter Jacket", "Sweatpants"
            ],
            "Home Appliances": [
                "Microwave Oven", "Refrigerator", "Ceiling Fan", "Electric Kettle", "Washing Machine"
            ],
            "Stationery": [
                "Notebook", "Ballpoint Pen", "Highlighter Set", "Sketchbook", "Glue Stick"
            ]
        }

        for category_name, product_list in category_product_map.items():
            slug = category_name.lower().replace(" ", "-")
            category, created = Category.objects.get_or_create(name=category_name, slug=slug)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category_name}'))

            for product_name in product_list:
                product = Product.objects.create(
                    name=product_name,
                    category=category,
                    description=f"{product_name} - High quality and affordable.",
                    price=round(random.uniform(10.0, 999.0), 2),
                    stock=random.randint(10, 200),
                )
                self.stdout.write(self.style.SUCCESS(f'Added product: {product.name} under {category.name}'))
