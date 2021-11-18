from rest_framework import authentication
from question.models import Option
from .serializers import OptionSerializer
from rest_framework import viewsets


class OptionViewSet(viewsets.ModelViewSet):
    serializer_class = OptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Option.objects.all()
