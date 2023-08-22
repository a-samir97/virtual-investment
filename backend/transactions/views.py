from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from .constants import QUANTITY_EXCEEDS_MSG_ERR, INSUFFICIENT_BALANCE_MSG_ERR
from stocks.models import Stock
from accounts.models import Account

class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @transaction.atomic()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        stock = Stock.objects.select_for_update().filter(id=serializer.validated_data['stock'].id).first()
        account = Account.objects.select_for_update().filter(id=serializer.validated_data['account'].id).first()

        # check if the requested quantity is greater than
        if stock.quantity < serializer.validated_data['quantity']:
            return Response({'error': QUANTITY_EXCEEDS_MSG_ERR}, status=status.HTTP_400_BAD_REQUEST)

        # check if balance already can purchase the order
        if account.balance < serializer.validated_data['quantity'] * stock.price:
            return Response({'error': INSUFFICIENT_BALANCE_MSG_ERR}, status=status.HTTP_400_BAD_REQUEST)

        # decrease balance
        account.balance -= (serializer.validated_data['quantity'] * stock.price)
        stock.quantity -= serializer.validated_data['quantity']

        # save objects after changes
        account.save()
        stock.save()

        # create transaction object
        transaction = Transaction.objects.create(
            stock=stock,
            account=account,
            quantity=serializer.validated_data['quantity'],
            purchase_price=stock.price,
        )
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
