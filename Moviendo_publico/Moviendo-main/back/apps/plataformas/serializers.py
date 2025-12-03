from rest_framework import serializers
from .models import Plataforma


class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'


class PlataformaSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = ['id', 'nome']
