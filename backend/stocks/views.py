from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from rest_framework.decorators import action


class StockModelViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    @action(methods=['GET'], detail=False)
    def recent(self, request, *args, **kwargs):
        serializer = StockSerializer(Stock.objects.all().order_by('-created_at')[:3], many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
