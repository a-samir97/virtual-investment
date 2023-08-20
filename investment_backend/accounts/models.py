from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(unique=True)


class Account(models.Model):
    customer = models.ForeignKey(Customer, related_name='accounts', on_delete=models.CASCADE)
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
