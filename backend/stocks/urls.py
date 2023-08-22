from rest_framework.routers import DefaultRouter
from .views import StockModelViewSet

router = DefaultRouter()
router.register('stocks', StockModelViewSet, basename='stocks')

urlpatterns = router.urls
