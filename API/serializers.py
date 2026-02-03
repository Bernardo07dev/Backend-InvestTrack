from rest_framework import serializers
from .models import User, Investimentos, Carteira, Transacao

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class InvestimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investimentos
        fields = ['id', 'user', 'stock', 'ticker', 'quantidade', 'data', 'price', 'total','img']

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = ['id', 'user', 'investido', 'saldo']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'carteira', 'transaction', 'data', 'tipo']