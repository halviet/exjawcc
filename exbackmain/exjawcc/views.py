from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *


class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


# Release View / Retrieve, Update, Create, List
class ReleaseRetrieveView(generics.RetrieveAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'


class ReleaseUpdateView(generics.UpdateAPIView):
    # queryset = Release.objects.all()
    serializer_class = CreateReleaseSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Release.objects.filter(user=user)

        raise PermissionDenied()


class ReleaseCreateView(generics.CreateAPIView):
    queryset = Release.objects.all()
    serializer_class = CreateReleaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReleaseListView(generics.ListAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        queryset = Release.objects.all()
        params = self.request.query_params
        slug = params.get('slug', None)

        if slug:
            queryset = queryset.filter(slug=slug)

        return queryset


# Platform View / Retrieve, Update, Create, List
class PlatformRetrieveView(generics.RetrieveAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformUpdateView(generics.UpdateAPIView):
    queryset = Platform.objects.all()
    serializer_class = CreatePlatformSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PlatformCreateView(generics.CreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = CreatePlatformSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PlatformListView(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer



# Link View / Retrieve, Update, Create, List
class LinkRetrieveView(generics.RetrieveAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkUpdateView(generics.UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = CreateLinkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LinkCreateView(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = CreateLinkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LinkListView(generics.ListAPIView):
    serializer_class = LinkSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Link.objects.all()
        params = self.request.query_params
        release = params.get('release', None)

        if release:
            queryset = queryset.filter(release=release)

        return queryset
