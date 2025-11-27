from rest_framework import serializers
from .models import Avaliacao
from apps.obras.serializers import ObraSummarySerializer


class AvaliacaoSerializer(serializers.ModelSerializer):
    obra_info = ObraSummarySerializer(source='obra', read_only=True)
    class Meta:
        model = Avaliacao
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.obras.models import Obra
        self.fields['obra'] = serializers.PrimaryKeyRelatedField(
            queryset=Obra.objects.all(),
            write_only=True
        )


class AvaliacaoSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ['id', 'nota', 'data_avaliacao']
