from rest_framework import serializers
from .models import Obra
from apps.diretores.serializers import DiretorSummarySerializer
from apps.generos.serializers import GeneroSummarySerializer
from apps.plataformas.serializers import PlataformaSummarySerializer
from apps.tags.serializers import TagSummarySerializer


class ObraSerializer(serializers.ModelSerializer):
    diretores_info = DiretorSummarySerializer(source='diretores', many=True, read_only=True)
    generos_info = GeneroSummarySerializer(source='generos', many=True, read_only=True)
    plataformas_info = PlataformaSummarySerializer(source='plataformas', many=True, read_only=True)
    tags_info = TagSummarySerializer(source='tags', many=True, read_only=True)
    
    class Meta:
        model = Obra
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from apps.diretores.models import Diretor
        from apps.generos.models import Genero
        from apps.plataformas.models import Plataforma
        from apps.tags.models import Tag
        
        self.fields['diretores'] = serializers.PrimaryKeyRelatedField(
            many=True, 
            queryset=Diretor.objects.all(), 
            write_only=True, 
            required=False
        )
        self.fields['generos'] = serializers.PrimaryKeyRelatedField(
            many=True, 
            queryset=Genero.objects.all(), 
            write_only=True, 
            required=False
        )
        self.fields['plataformas'] = serializers.PrimaryKeyRelatedField(
            many=True, 
            queryset=Plataforma.objects.all(), 
            write_only=True, 
            required=False
        )
        self.fields['tags'] = serializers.PrimaryKeyRelatedField(
            many=True, 
            queryset=Tag.objects.all(), 
            write_only=True, 
            required=False
        )


class ObraSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['id', 'titulo', 'tipo', 'status', 'ano_lancamento']


class ImportarTmdbSerializer(serializers.Serializer):
    tmdb_id = serializers.IntegerField()
    tipo = serializers.ChoiceField(choices=['movie', 'tv'])
