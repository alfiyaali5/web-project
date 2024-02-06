from django.db import models

# Create your models here.

# Create your models here.

class Products(models.Model):
    def __str__(self)-> str:
         return self.title
    
    title=models.CharField(max_length=200)
    price=models.FloatField(null=True)
    discount_price=models.FloatField()
    category=models.CharField(max_length=200)
    discription=models.TextField()
    image=models.CharField(max_length=300)