from rest_framework import serializers
from .models import User  # Import your User model here

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']