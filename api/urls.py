from django.urls import include, path
from rest_framework import routers
from .views import DessertViewSet

router = routers.DefaultRouter()
router.register(r'dessert', DessertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
