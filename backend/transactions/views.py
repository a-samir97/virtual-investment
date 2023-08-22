from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from stocks.models import Stock


class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    # def create(self, request, *args, **kwargs):
    #     with transaction.atomic():
    #         serializer = self.get_serializer(data=request.data)
    #         serializer.is_valid(raise_exception=True)
    #         stock = Stock.objects.select_for_update().filter(id=serializer.validated_data['stock'].id).first()
    #         if serializer.validated_data['account'].balance >= serializer.validated_data['quantity'] * stock.price and \
    #                 stock.quantity >= serializer.validated_data['quantity']:
    #             serializer.validated_data['account'].balance -= serializer.validated_data['quantity'] * stock.price
    #             stock.quantity -= serializer.validated_data['quantity']
    #             stock.save()
    #             serializer.save()
    #             return Response({"message": "Done"}, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)