from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from app.start.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_class = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permissions_class = [permissions.IsAuthenticated]
