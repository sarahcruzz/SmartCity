# Importando as libs 
from django.contrib.auth.models import User # Importando o models User já criado pelo django
from rest_framework import serializers # importando o serializer do rest 
from django.contrib.auth.hashers import make_password # permite criptografar a senha
from app_smart.models import Sensor


class UserSerializer (serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    extra_kwargs = {'password':{'write_only': True} } # diz que se quiser consumir uma 
                                                      #senha ele não vai retorná-la


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor #tabela no banco de dados 
        fields = '__all__' #está permitindo o tráfego de dados de todos os campos 
