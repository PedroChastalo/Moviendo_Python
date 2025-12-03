from rest_framework.routers import DefaultRouter
from .views import PlataformaViewSet

router = DefaultRouter()
router.register(r'plataformas', PlataformaViewSet)

urlpatterns = router.urls
