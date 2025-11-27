from rest_framework import serializers
from .models import Genero


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class GeneroSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']
