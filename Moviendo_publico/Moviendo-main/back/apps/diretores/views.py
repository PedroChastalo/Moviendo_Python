from rest_framework import viewsets
from .models import Diretor
from .serializers import DiretorSerializer


class DiretorViewSet(viewsets.ModelViewSet):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer
