from rest_framework.routers import DefaultRouter
from .views import GeneroViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet)

urlpatterns = router.urls
