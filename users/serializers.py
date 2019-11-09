from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework.exceptions import APIException
from rest_framework import serializers


class AdminUserSerializer(serializers.ModelSerializer):
    """Serializer for user model"""
    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'last_name',
                  'first_name', 'middle_name', 'phone')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        if email:
            validated_data['email'] = email.lower()
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if(password):
            user.set_password(password)
            user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model"""
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'last_name',
                  'first_name', 'middle_name', 'phone', )
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        email = validated_data.pop('email', None)
        validated_data['email'] = email.strip().lower()
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update a user setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if(password):
            user.set_password(password)
            user.save()
        return user
