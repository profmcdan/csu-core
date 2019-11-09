from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import serializers
from .models import Profile


class DefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = []


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['created_on', 'modified_on', 'user']
