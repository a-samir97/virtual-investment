from rest_framework.routers import DefaultRouter
from .views import CustomerModelViewSet, AccountsViewSet

router = DefaultRouter()

router.register('customers', CustomerModelViewSet, basename='customers')
router.register('accounts', AccountsViewSet, basename='accounts')

urlpatterns = router.urls
