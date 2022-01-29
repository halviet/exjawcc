from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class ReleaseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    cover_resized = serializers.ImageField(read_only=True)

    class Meta:
        model = Release
        fields = '__all__'
        lookup_field = 'slug'


class ReleaseIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id']


class CreateReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):
    platform_type = serializers.CharField(source='get_platform_type_display')

    class Meta:
        model = Platform
        fields = '__all__'


class CreatePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    release = ReleaseIdSerializer()
    platform = PlatformSerializer()

    class Meta:
        model = Link
        fields = '__all__'


class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
