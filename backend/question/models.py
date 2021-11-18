from django.conf import settings
from django.db import models


class Option(models.Model):
    "Generated Model"
    option_name = models.CharField(
        max_length=256,
    )


class Question(models.Model):
    "Generated Model"
    question_name = models.CharField(
        max_length=256,
    )
    input_type_id = models.ForeignKey(
        "question.InputType",
        on_delete=models.CASCADE,
        related_name="question_input_type_id",
    )


class QuestionOption(models.Model):
    "Generated Model"
    question_id = models.ForeignKey(
        "question.Question",
        on_delete=models.CASCADE,
        related_name="questionoption_question_id",
    )
    option_id = models.ForeignKey(
        "question.Option",
        on_delete=models.CASCADE,
        related_name="questionoption_option_id",
    )


class Answer(models.Model):
    "Generated Model"
    answer = models.CharField(
        max_length=256,
    )
    user_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="answer_user_id",
    )
    question_option_id = models.ForeignKey(
        "question.QuestionOption",
        on_delete=models.CASCADE,
        related_name="answer_question_option_id",
    )


class InputType(models.Model):
    "Generated Model"
    input_type_name = models.CharField(
        max_length=256,
    )


# Create your models here.
