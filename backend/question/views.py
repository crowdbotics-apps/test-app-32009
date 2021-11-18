from django.shortcuts import render

# Create your views here.

def user_profile(request):
  user_data = Answer.objects.filter(user_id=request.POST['user_id'])
  return user_data
