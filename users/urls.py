from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.UserViewSet)

app_name = 'users'


urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register, name='reg'),
]
