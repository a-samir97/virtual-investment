from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=256, null=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
