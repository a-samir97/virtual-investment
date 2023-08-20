from rest_framework.routers import DefaultRouter
from .views import TransactionModelViewSet

router = DefaultRouter()

router.register('transactions', TransactionModelViewSet, basename='transactions')

urlpatterns = router.urls
