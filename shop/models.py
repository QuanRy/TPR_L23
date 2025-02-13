from django.db import models

# Create your models here. (first commit)
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=200)

    def calculate_discounted_price(self, is_discount_applicable):
        """
        Возвращает цену товара с учетом скидки.
        """
        if is_discount_applicable:
            return self.price * 0.6 
        return self.price


class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    person = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)