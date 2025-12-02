from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AvaliacaoViewSet

router = DefaultRouter()
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('avaliacoes/obra/<int:obra_pk>/', AvaliacaoViewSet.as_view({'get': 'by_obra'}), name='avaliacao-by-obra'),
] + router.urls
