from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from didConfiguration import views

router = routers.DefaultRouter()
router.register(r'did-configurations\.json', views.DidConfigurationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
