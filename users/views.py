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
	'''
	Django REST Framework ViewSet for the User Model

	Includes the queryset for the GET endpoint, as well as the 
	serializer for all responses.

	GET, POST, PUT, DELETE functionality are automated with the ViewSet.
	'''
	queryset = User.objects.all().order_by('last_name')
	serializer_class = UserSerializer

# /api/users/{userId}/tasks/
@csrf_exempt
def tasks_view(request, pk):
	'''
	View for functionality related to tasks for a specified user.

	Parameters:
		request - Django request object
		pk - userId for the relevant user.

	Returns:
		HttpResponse or JsonResponse object.
	'''
	
	# Determines if the provided userId is valid.
	# 	Returns 404 error code if invalid.
	relevant_user = None
	try:
		relevant_user = User.objects.get(pk = pk)
	except:
		return HttpResponse(status_code = 404, content = "No user found.")	

	# GET
	if request.method == 'GET':
		tasks = Task.objects.filter(user__pk=pk)
		task_list = [TaskSerializer(task).data for task in tasks]
		return JsonResponse({'context': task_list})	
	# POST
	elif request.method == 'POST':
		# TODO: Json check and throws error.
		json_body = json.loads(request.body)
		q = Task(user=relevant_user, \
			subject = json_body['subject'], \
			length = float(json_body['length']), \
			difficulty = int(json_body['difficulty']))
		q.save()
		return JsonResponse(TaskSerializer(q).data)
	# TODO: DELETE
	# TODO: PUT
