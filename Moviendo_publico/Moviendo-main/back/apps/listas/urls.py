from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListaViewSet

router = DefaultRouter()
router.register(r'listas', ListaViewSet)

urlpatterns = [
    path('listas/<int:pk>/obras/<int:obra_pk>/', ListaViewSet.as_view({'post': 'manage_obra', 'delete': 'manage_obra'}), name='lista-manage-obra'),
] + router.urls
