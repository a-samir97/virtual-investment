from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['name'] = instance.stock.name
        data['gain_loss'] = (instance.stock.price - instance.purchase_price) * instance.quantity
        data['current_price'] = instance.stock.price
        data['created_at'] = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return data
