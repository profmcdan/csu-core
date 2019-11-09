from rest_framework.decorators import action
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """Create a new user in the system"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
