from django.db import models
from django.db import models
from django.contrib.auth.models import User


# Modelo del Perfil del usuario
class Profile(models.Model):
    ROLES = (
        ('superadmin', 'superAdmin'),
        ('admin', 'AdminTorneos'),
        ('player', 'Jugador'),
        
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relación 1 a 1 con User
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLES)
    
    
    def __str__(self):
        return f'Perfil de {self.user.username} - {self.role}'

