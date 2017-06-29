from django.contrib.auth.models import Group
from django.shortcuts import render

# Create your views here.
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework import viewsets, filters

from TestAuth import serializers, models
from TestAuth.serializers import GroupSerializer
from TestAuth.permissions import UpdateOwnProfile, IsAuthenticatedOrCreate, IsOwnerOrReadOnly

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    Handles creating, creating and updating profiles.
    ModelViewset Creates, Reads, update object on model.
    """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (IsAuthenticatedOrCreate, IsOwnerOrReadOnly)



class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer