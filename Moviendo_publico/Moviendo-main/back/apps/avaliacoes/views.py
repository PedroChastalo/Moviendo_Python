from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Avaliacao
from .serializers import AvaliacaoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    @action(detail=False, methods=['get'])
    def by_obra(self, request, obra_pk=None):
        queryset = self.get_queryset().filter(obra_id=obra_pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
