from rest_framework import serializers
from .models import User
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

