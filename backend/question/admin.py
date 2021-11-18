from django.contrib import admin
from .models import Answer, InputType, Option, Question, QuestionOption

admin.site.register(Option)
admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(Answer)
admin.site.register(InputType)

# Register your models here.
