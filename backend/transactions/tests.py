from django.test import TestCase
from .models import Transaction
from accounts.models import Account, Customer
from stocks.models import Stock
from rest_framework import status
from .constants import QUANTITY_EXCEEDS_MSG_ERR, INSUFFICIENT_BALANCE_MSG_ERR


class TransactionTest(TestCase):

    def setUp(self) -> None:
        self.transaction_url = '/api/transactions/'
        self.transaction_detail_url = '/api/transactions/{}/'

        self.customer = Customer.objects.create(name='customer', email='customer@gmail.com')
        self.account = Account.objects.create(customer=self.customer, balance=100.00)
        self.stock = Stock.objects.create(name='Adcash', price=20.00, quantity=20)

    def test_create_transaction_success_case(self):
        data = {
            'stock': self.stock.id,
            'account': self.account.id,
            'quantity': 5,
        }
        response = self.client.post(self.transaction_url, data=data)

        self.account.refresh_from_db()
        self.stock.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(self.account.balance, 0)
        self.assertEquals(self.stock.quantity, 15)

    def test_create_transaction_failure_case_quantity_exceeds(self):
        data = {
            'stock': self.stock.id,
            'account': self.account.id,
            'quantity': 100,
        }
        response = self.client.post(self.transaction_url, data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['error'], QUANTITY_EXCEEDS_MSG_ERR)

    def test_create_transaction_failure_case_unsufficient_balance(self):
        data = {
            'stock': self.stock.id,
            'account': self.account.id,
            'quantity': 11,
        }
        response = self.client.post(self.transaction_url, data=data)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(response.data['error'], INSUFFICIENT_BALANCE_MSG_ERR)
