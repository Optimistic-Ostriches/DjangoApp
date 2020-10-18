from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Django REST Framework serializer for the User model.
	'''
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email_address']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
	'''
	Django REST Framework serializer for the Task model.
	'''
	class Meta:
		model = Task
		fields = ['pk', 'subject', 'length', 'difficulty', 'due_date']