from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Lista
from apps.obras.models import Obra
from .serializers import ListaSerializer


class ListaViewSet(viewsets.ModelViewSet):
    queryset = Lista.objects.all()
    serializer_class = ListaSerializer

    def manage_obra(self, request, pk=None, obra_pk=None):
        lista = self.get_object()
        try:
            obra = Obra.objects.get(pk=obra_pk)
        except Obra.DoesNotExist:
            return Response({'detail': 'Obra não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'POST':
            lista.obras.add(obra)
            return Response({'detail': 'Obra adicionada à lista com sucesso.'}, status=status.HTTP_200_OK)
        
        elif request.method == 'DELETE':
            lista.obras.remove(obra)
            return Response({'detail': 'Obra removida da lista com sucesso.'}, status=status.HTTP_204_NO_CONTENT)
