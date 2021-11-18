from rest_framework import serializers
from question.models import Answer, InputType, Option, Question, QuestionOption


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


class InputTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputType
        fields = "__all__"
