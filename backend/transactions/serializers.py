from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='stock.name', read_only=True)
    current_price = serializers.CharField(source='stock.price', read_only=True)
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    gain_loss = serializers.SerializerMethodField(read_only=True)
    purchase_price = serializers.CharField(read_only=True)
    
    class Meta:
        model = Transaction
        fields = '__all__'

    def get_gain_loss(self, instance):
        return str((instance.stock.price - instance.purchase_price) * instance.quantity)
