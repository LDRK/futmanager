from django.urls import path
from accounts.api.api import user_api_view, user_details_view
from accounts.views import login

urlpatterns = [
    path('users/', user_api_view, name='users_api'),
    path('users/<int:pk>/', user_details_view, name='users_details_api'),
    path('login/', login, name='login')
]