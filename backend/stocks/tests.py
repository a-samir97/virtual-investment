from django.test import TestCase
from .models import Stock
from rest_framework import status


class StockTests(TestCase):

    def setUp(self) -> None:
        self.stock = Stock.objects.create(name='test', quantity=10, price=10.25)
        self.stock_url = '/api/stocks/'
        self.stock_detail_url = '/api/stocks/{id}/'

    def test_create_stock_success_case(self):
        oldCount = Stock.objects.count()

        data = {
            'name': 'New Stock',
            'quantity': 120,
            'price': 15.00
        }
        response = self.client.post(self.stock_url, data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(oldCount + 1, Stock.objects.count())

    def test_create_stock_failure_case_no_data(self):
        response = self.client.post(self.stock_url)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_stock_success_case(self):
        response = self.client.get(self.stock_detail_url.format(id=self.stock.id))

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['name'], self.stock.name)
        self.assertEquals(response.data['quantity'], self.stock.quantity)
        self.assertEquals(response.data['price'], str(self.stock.price))

    def test_get_stock_failure_case_not_found(self):
        response = self.client.get(self.stock_detail_url.format(id=10000000)) # invalid id

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_stock_success_case(self):

        data = {
            'name': 'Adcash'
        }

        response = self.client.patch(self.stock_detail_url.format(id=self.stock.id), data=data, 
                                     content_type='application/json')
        # refresh database after change
        self.stock.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(data['name'], self.stock.name)

    def test_update_stock_failure_case_no_data(self):

        response = self.client.put(self.stock_detail_url.format(id=self.stock.id))

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
