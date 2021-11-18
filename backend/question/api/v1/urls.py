from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OptionViewSet

router = DefaultRouter()
router.register("option", OptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
