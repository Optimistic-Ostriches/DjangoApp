from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer, TaskSerializer
from .models import User, Task
import json


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('last_name')
	serializer_class = UserSerializer

@csrf_exempt
def tasks_view(request, pk):
	relevant_user = None
	try:
		relevant_user = User.objects.get(pk = pk)
	except:
		return HttpResponse("No user found.")	

	if request.method == 'GET':
		tasks = Task.objects.filter(user__pk=pk)
		task_list = [TaskSerializer(task).data for task in tasks]
		return JsonResponse({'context': task_list})	
	elif request.method == 'POST':
		json_body = json.loads(request.body)
		q = Task(user=relevant_user, \
			subject = json_body['subject'], \
			length = float(json_body['length']), \
			difficulty = int(json_body['difficulty']))
		q.save()
		return JsonResponse(TaskSerializer(q).data)
