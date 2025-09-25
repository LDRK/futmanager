from django.contrib.auth.models import User
from accounts.models import Profile
from rest_framework import serializers

# Serializamos el modelo Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nombre','apellido','telefono','role']
        
# Serializamos le modelo User
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    
    class Meta:
        model = User
        fields = ['id','username','password','email','profile']
        # El campo se puede enviar en requests (POST/PUT), pero no se muestra en responses (GET).
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        # extraer datos del perfil
        profile_data = validated_data.pop('profile')

        # crear el usuario con contraseña encriptada
        user = User.objects.create_user(**validated_data)

        # crear perfil vinculado
        Profile.objects.create(user=user, **profile_data)

        return user

    def update(self, instance, validated_data):
        # Extraemos los datos del perfil
        profile_data = validated_data.pop('profile', None)

        # Actualizamos datos básicos del usuario
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # Solo actualizamos contraseña si viene en el request
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        instance.save()

        # Si viene perfil, lo actualizamos
        if profile_data:
            profile = instance.profile
            profile.nombre = profile_data.get('nombre', profile.nombre)
            profile.apellido = profile_data.get('apellido', profile.apellido)
            profile.telefono = profile_data.get('telefono', profile.telefono)
            profile.role = profile_data.get('role', profile.role)
            profile.save()

        return instance
