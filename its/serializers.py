from rest_framework import serializers
from .models import *
from django.contrib.auth.models import Group, Permission




class AuthTokenSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AuthToken
        fields =['token']