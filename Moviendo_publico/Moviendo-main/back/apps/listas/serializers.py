from rest_framework import serializers
from .models import Lista
from apps.obras.serializers import ObraSummarySerializer


class ListaSerializer(serializers.ModelSerializer):
    obras_info = ObraSummarySerializer(source='obras', many=True, read_only=True)
    total_obras = serializers.ReadOnlyField()

    class Meta:
        model = Lista
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.obras.models import Obra
        self.fields['obras'] = serializers.PrimaryKeyRelatedField(
            many=True,
            queryset=Obra.objects.all(),
            write_only=True,
            required=False
        )


class ListaSummarySerializer(serializers.ModelSerializer):
    total_obras = serializers.ReadOnlyField()
    
    class Meta:
        model = Lista
        fields = ['id', 'nome', 'tipo', 'total_obras']
