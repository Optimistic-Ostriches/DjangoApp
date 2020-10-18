from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email_address']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Task
		fields = ['pk', 'subject', 'length', 'difficulty', 'due_date']