from django.urls import path, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'doc'

schema_view = get_schema_view(
    openapi.Info(
        title="TEDx API",
        default_version='v3',
        description="API Docs",
        terms_of_service="Just Break The Fucking Rules...",
        contact=openapi.Contact(email="mohammadmoallemi@outlook.com"),
        license=openapi.License(name="GPL v2"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
