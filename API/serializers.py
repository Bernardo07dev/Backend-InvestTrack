from rest_framework import serializers
from .models import User, Investimento

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'senha']

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimento
        fields = ['id', 'user', 'stock', 'ticker', 'quantidade', 'data', 'price']