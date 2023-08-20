from rest_framework.viewsets import ModelViewSet
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionModelViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
