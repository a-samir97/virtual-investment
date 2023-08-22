from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Phonebook API",
      default_version='v1',
      description="Phonebook API endpoints",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Admin page
    path("admin/", admin.site.urls),

    # APIs endpoints
    path("api/", include("stocks.urls")),
    path("api/", include("accounts.urls")),
    path("api/", include("transactions.urls")),

    # Swagger documenation
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
