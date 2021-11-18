from django.shortcuts import render
from .models import Answer, InputType, Option, Question, QuestionOption

# Create your views here.

def user_profile(request):
  user_data = Answer.objects.filter(user_id=1)#request.POST['user_id']
  return {'name':'chirag'}
  return user_data
