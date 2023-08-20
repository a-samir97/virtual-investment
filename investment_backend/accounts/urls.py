from rest_framework.routers import DefaultRouter
from .views import CustomerModelViewSet

router = DefaultRouter()

router.register('customers', CustomerModelViewSet, basename='customers')

urlpatterns = router.urls
