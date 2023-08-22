from django.db import models
from django.db.models import Sum, F


class Customer(models.Model):
    name = models.CharField(max_length=256, null=False)
    email = models.EmailField(unique=True)


class Account(models.Model):
    customer = models.OneToOneField(Customer, related_name='account', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.customer.name + ' | ' + str(self.balance)

    @property
    def total_gain_loss(self):
        result = self.transactions.aggregate(
            total_gain_loss=Sum(
                (
                    F('stock__price') - F('purchase_price')
                ) * (
                    F('quantity')
                ), output_field=models.DecimalField(max_digits=10, decimal_places=2)
            )
        )['total_gain_loss']

        return result

    @property
    def total_portfolio_value(self):
        result = self.transactions.aggregate(
            total_portfolio_value=Sum(
                F('quantity') *
                F('stock__price'), output_field=models.DecimalField(max_digits=10, decimal_places=2)))['total_portfolio_value']
        return result
