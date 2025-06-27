from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=20)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveBigIntegerField()
    image=models.ImageField(upload_to="products/",blank=True,null=True)
    @property
    def in_stock(self):
        if self.stock>0:
            return True
        return False
    
    def  __str__(self):
        return self.name
