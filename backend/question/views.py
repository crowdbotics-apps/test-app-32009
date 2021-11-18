from django.shortcuts import render
from .models import Answer, InputType, Option, Question, QuestionOption

# Create your views here.

def user_profile(request):
  user_data = Answer.objects.filter(user_id=request.POST['user_id'])
  return user_data
