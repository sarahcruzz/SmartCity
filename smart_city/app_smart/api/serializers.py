from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    # realizando a tratativa dos dados
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta: 
        model = User
        fields = ['id', 'username', 'email', 'password']

    extra_kwargs = {'password': {'write_only': True}} # não permite que a senha seja consumida, apenas cadastrada no banco 
