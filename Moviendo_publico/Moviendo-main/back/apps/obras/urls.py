from rest_framework.routers import DefaultRouter
from .views import ObraViewSet

router = DefaultRouter()
router.register(r'obras', ObraViewSet)

urlpatterns = router.urls
