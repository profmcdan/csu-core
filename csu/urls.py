"""csu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from users import views

from .schema import schema

schema_view = get_schema_view(
    openapi.Info(
        title="CSU GF API",
        default_version='v1',
        description="C&S Unification Graduate Forum Akure API Doc",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="danielale9291@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    url(r'^doc/$', schema_view.with_ui('swagger',
                                       cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('api', csrf_exempt(FileUploadGraphQLView.as_view(
        graphiql=True, schema=schema))),
    path('api/auth/register', views.register, name='regit'),
    path('api/auth/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/auth/refresh-token/',
         jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/', include('users.urls')),
    path('api/profile/', include('members.urls')),

]
