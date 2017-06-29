from django.contrib.auth.models import Group
from rest_framework import serializers

from TestAuth import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""


    # meta class 는 모델에서 무슨 field를 뽑아 사용할지를 DRF에게 말해주는 것.
    # password 필드는 no read, no see!! 시리얼라이저로 단지 write만 가능.
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # Override create function
    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')