from rest_framework import serializers
from .models import User, Investimentos

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'senha']

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimentos
        fields = ['id', 'user', 'stock', 'ticker', 'quantidade', 'data', 'price', 'total']