from django.db.models import F, Sum, DecimalField
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from .models import Customer, Account
from .serializers import CustomerSerializer, AccountsSerializer, MostProfitableClientsSerializer
from rest_framework.decorators import action
from transactions.models import Transaction


class CustomerModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def perform_create(self, serializer):
        super().perform_create(serializer)
        # link every customer to account
        # every customer must has only one account
        # for now default balance is 0
        Account.objects.create(customer=serializer.instance)


class AccountsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer

    @action(methods=['GET'], detail=False)
    def most_profitable(self, request, *args, **kwargs):
        most_profitable_clients = Transaction.objects.values('account', name=F('account__customer__name')).annotate(total=Sum((
                    F('stock__price') - F('purchase_price')
                ) * (
                    F('quantity')
                ), output_field=DecimalField())).order_by('-total')[:3]
        serializer = MostProfitableClientsSerializer(most_profitable_clients, many=True)
        return Response(serializer.data)
