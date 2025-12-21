from django.http import HttpResponse
from .models import User, Investimentos
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, InvestimentoSerializer, CarteiraSerializer, TransacaoSerializer
from .models import Carteira, Transacao
from django.utils import timezone

@api_view(['GET', 'DELETE', 'POST']) 
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Usuário não encontrado")

@api_view(['GET', 'DELETE', 'POST']) 
def verify(request):
    email = request.data.get('email')
    senha = request.data.get('senha')
    try:
        user = User.objects.get(email=email, senha=senha)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except Exception as e:
        return Response({"erro_detalhado": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'POST'])  
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        Carteira.objects.create(
            user=user
        )
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST']) 
def create_investimento(request):
    serializer = InvestimentoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])    
def get_investimentos(request):
    user_id = request.data.get('user')

    investimentos = Investimentos.objects.filter(user=user_id)
    serializer = InvestimentoSerializer(investimentos, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_transaction(request):
    user = request.user
    try:
        carteira = Carteira.objects.get(user=user)
        valor = request.data.get('valor')
        tipo = request.data.get('tipo')

        if tipo == 'adicionar':
            carteira.saldo += valor
        elif tipo == 'subtrair':
            carteira.saldo -= valor
            carteira.investido += valor

        Transacao.objects.create(
            carteira=carteira,
            transaction=valor,
            tipo=tipo,
            data=timezone.now()
        )

        return Response(
            {'mensagem': 'Transação realizada com sucesso'},
            status=status.HTTP_201_CREATED
        )
    
    except Carteira.DoesNotExist:
        return Response(
            {'erro': 'Carteira não encontrada'},
            status=status.HTTP_404_NOT_FOUND
        )