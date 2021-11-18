from django.urls import path, include
from rest_framework.routers import DefaultRouter
from question import views
from . import views
from .viewsets import (
    AnswerViewSet,
    InputTypeViewSet,
    OptionViewSet,
    QuestionViewSet,
    QuestionOptionViewSet,
)

router = DefaultRouter()
router.register("option", OptionViewSet)
router.register("question", QuestionViewSet)
router.register("questionoption", QuestionOptionViewSet)
router.register("answer", AnswerViewSet)
router.register("inputtype", InputTypeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('profile/', views.user_profile, name='user_profile'),
]
