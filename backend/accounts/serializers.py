from rest_framework import serializers
from .models import Customer, Account
from transactions.serializers import TransactionSerializer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['account'] = instance.account.id
        return data


class AccountsSerializer(serializers.ModelSerializer):
    total_gain_loss = serializers.CharField()
    total_portfolio_value = serializers.CharField()

    class Meta:
        model = Account
        fields = ['balance', 'total_gain_loss', 'total_portfolio_value']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['transactions'] = TransactionSerializer(instance.transactions.all(), many=True).data
        data['name'] = instance.customer.name
        return data


class MostProfitableClientsSerializer(serializers.Serializer):
    name = serializers.CharField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    account = serializers.IntegerField()