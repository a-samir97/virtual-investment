from django.db import models

from stocks.models import Stock
from accounts.models import Account

BUY = 1
SELL = 2
TRANSACTION_TYPE = (
    (BUY, 'Buy'),
    (SELL, 'Sell')
)


class Transaction(models.Model):
    stock = models.ForeignKey(Stock, related_name='transactions', on_delete=models.CASCADE)
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    purchase_price = models.FloatField(default=0.0)
    type = models.IntegerField(choices=TRANSACTION_TYPE, default=BUY)
    created_at = models.DateTimeField(auto_now_add=True)
