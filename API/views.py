from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

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
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

