from django.db import models

# Create your models here.
class Product(models.Model):

    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    product_qty = models.CharField(max_length=12)
    product_prize = models.IntegerField()


def __str__(self) -> str:
    return f"{self.product_name} {self.product_qty} {self.product_prize}"