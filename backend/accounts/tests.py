from django.test import TestCase
from .models import Account, Customer
from rest_framework import status


class CustomerTests(TestCase):

    def setUp(self) -> None:
        self.customer = Customer.objects.create(name='test', email='test@gmail.com')
        self.account = Account.objects.create(balance=1000.00, customer=self.customer)
        self.customer_url = '/api/customers/'
        self.customer_detail_url = '/api/customers/{id}/'

    def test_create_customer_success_case(self):
        oldCount = Customer.objects.count()

        data = {
            'name': 'Customer 1',
            'email': 'customer1@gmail.com',
        }
        response = self.client.post(self.customer_url, data=data)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(oldCount + 1, Customer.objects.count())

    def test_create_customer_failure_case_no_data(self):
        response = self.client.post(self.customer_url)

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_stock_customer_case(self):
        response = self.client.get(self.customer_detail_url.format(id=self.customer.id))

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['name'], self.customer.name)
        self.assertEquals(response.data['email'], self.customer.email)

    def test_get_customer_failure_case_not_found(self):
        response = self.client.get(self.customer_detail_url.format(id=10000000)) # invalid id

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_customer_success_case(self):

        data = {
            'name': 'Customer 2'
        }

        response = self.client.patch(self.customer_detail_url.format(id=self.customer.id), data=data, 
                                     content_type='application/json')
        # refresh database after change
        self.customer.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(data['name'], self.customer.name)

    def test_update_customer_failure_case_no_data(self):

        response = self.client.put(self.customer_detail_url.format(id=self.customer.id))

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class AccountTest(TestCase):

    def setUp(self) -> None:
        self.customter = Customer.objects.create(name='Customer1', email='customer@gmail.com')
        self.account = Account.objects.create(customer=self.customter, balance=10.00)

        self.account_url = '/api/accounts/'
        self.accounts_detail_url = '/api/accounts/{id}/'

    def test_list_all_accounts(self):
        response = self.client.get(self.account_url)

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_account_success_case(self):
        response = self.client.get(self.accounts_detail_url.format(id=self.account.id))

        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_account_failure_case_not_found(self):
        response = self.client.get(self.accounts_detail_url.format(id=100000)) # invalid id

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
