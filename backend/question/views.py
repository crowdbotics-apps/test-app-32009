from django.shortcuts import render
from .models import Answer, InputType, Option, Question, QuestionOption
from django.http import JsonResponse

# Create your views here.

def user_profile(request):
  user_data = Answer.objects.filter(user_id=1)#request.POST['user_id']
  print('user_data')
  print(user_data)
  print('type of : ', type(user_data))
  return JsonResponse(user_data)
