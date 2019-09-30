from django.contrib.auth.models import Group, User
from oauth2_provider.contrib.rest_framework import TokenHasResourceScope
from rest_framework import permissions, viewsets

from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasResourceScope]
    required_scopes = ["user_info"]
    queryset = User.objects.all()
    serializer_class = UserSerializer
