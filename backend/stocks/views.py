from rest_framework.viewsets import ModelViewSet
from .models import Stock
from .serializers import StockSerializer


class StockModelViewSet(ModelViewSet):
    queryset = Stock.objects.all().order_by('-created_at')[:3]
    serializer_class = StockSerializer
