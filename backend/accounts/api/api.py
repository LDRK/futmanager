from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.contrib.auth.models import User
from accounts.models import Profile
# from rest_framework.views import APIView
from rest_framework.decorators import api_view
from accounts.api.serializer import UserSerializer, ProfileSerializer

# Vistas Usuario

@api_view(['GET','POST'])
def user_api_view(request):
    """Vista API para listar todos los usuarios (GET) y crear nuevos (POST)"""
    
    if request.method == 'GET':
        # Obtener todos los usuarios y serializarlos
        users = User.objects.all()
        users_serizers = UserSerializer(users,many = True)
        return Response(users_serizers.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        # Crear nuevo usuario con validación
        user_serizers = UserSerializer(data = request.data)
        if user_serizers.is_valid():
            user_serizers.save()
            return Response({'message':'Usuario registrado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(user_serizers.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def user_details_view(request,pk=None):
    """Vista API para operaciones específicas de un usuario por ID"""
    
    # Buscar usuario por ID 
    user_id = User.objects.filter(id = pk).first()
    
    # user_id = get_object_or_404(User, id=pk)
    
    if user_id:
        
        if request.method == 'GET':
            # Obtener detalles del usuario específico
            user_serizers = UserSerializer(user_id)
            return Response(user_serizers.data, status = status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            # Actualizar usuario existente
            user_serizers = UserSerializer(user_id, data = request.data, partial=True)
            if user_serizers.is_valid():
                user_serizers.save()
                return Response({'message':'Registro actualizado correctamente'}, status = status.HTTP_201_CREATED)
            return Response(user_serizers.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            # Eliminar usuario
            user_id.delete()
            return Response({'message':'Registro eliminado correctamente'})
    
    else:
        # Usuario no encontrado
        return Response({'Error':'Pagina no encontrada'}, status=status.HTTP_404_NOT_FOUND)  
