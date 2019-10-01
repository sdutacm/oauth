from oauth2_provider.contrib.rest_framework import TokenHasResourceScope
from rest_framework import permissions, viewsets

from .models import UserEdu, UserInfo, UserPriv, UserSocial
from .serializers import (
    UserEduSerializer,
    UserInfoSerializer,
    UserPrivSerializer,
    UserSocialSerializer,
)


class UserInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasResourceScope]
    required_scopes = ["user_info"]
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class UserPrivViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasResourceScope]
    required_scopes = ["user_priv"]
    queryset = UserPriv.objects.all()
    serializer_class = UserPrivSerializer


class UserEduViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasResourceScope]
    required_scopes = ["user_edu"]
    queryset = UserEdu.objects.all()
    serializer_class = UserEduSerializer


class UserSocialViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasResourceScope]
    required_scopes = ["user_social"]
    queryset = UserSocial.objects.all()
    serializer_class = UserSocialSerializer
