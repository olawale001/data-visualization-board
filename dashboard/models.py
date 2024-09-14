from django.db import models


class SalesRecord(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.product 
