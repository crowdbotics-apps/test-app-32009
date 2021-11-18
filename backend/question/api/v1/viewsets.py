from rest_framework import authentication
from question.models import Answer, InputType, Option, Question, QuestionOption
from .serializers import (
    AnswerSerializer,
    InputTypeSerializer,
    OptionSerializer,
    QuestionSerializer,
    QuestionOptionSerializer,
)
from rest_framework import viewsets


class OptionViewSet(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Option.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Question.objects.all()


class QuestionOptionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionOptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = QuestionOption.objects.all()


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Answer.objects.all()


class InputTypeViewSet(viewsets.ModelViewSet):
    serializer_class = InputTypeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = InputType.objects.all()
