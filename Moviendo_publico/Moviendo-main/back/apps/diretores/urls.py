from rest_framework.routers import DefaultRouter
from .views import DiretorViewSet

router = DefaultRouter()
router.register(r'diretores', DiretorViewSet)

urlpatterns = router.urls
