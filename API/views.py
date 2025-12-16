from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer


def teste(request):
    return HttpResponse("<h1>Hello World<h1>")

@api_view(['GET', 'DELETE']) 
def get_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Usuário não encontrado")
    
def delete_user(request, user_id):
    return HttpResponse("Usuário deletado")
