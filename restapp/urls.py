from django.urls import path
from django.urls.conf import include
from restapp import views
from restapp.views import contactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', contactViewSet, basename='contact') 

urlpatterns = [
    path('',include(router.urls))
]
