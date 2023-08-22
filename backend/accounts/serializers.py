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
    class Meta:
        model = Account
        fields = ['balance']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['total_profit_loss'] = instance.total_gain_loss
        data['total_portfolio_value'] = instance.total_portfolio_value
        data['transactions'] = TransactionSerializer(instance.transactions.all(), many=True).data
        return data


class MostProfitableClientsSerializer(serializers.Serializer):
    name = serializers.CharField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    account = serializers.IntegerField()