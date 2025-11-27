from rest_framework.routers import DefaultRouter
from .views import ListaViewSet

router = DefaultRouter()
router.register(r'listas', ListaViewSet)

urlpatterns = router.urls
