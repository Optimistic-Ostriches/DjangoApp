from django.db import models

# Create your models here.

class User(models.Model):
	'''
	User model for the database.

	Fields:
		first_name - string
		last_name - string
		email_address - string
	'''
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	email_address = models.CharField(max_length = 200)

	def __str__(self):
		'''
		To string function.
		'''
		return "{} {} - {}".format(self.first_name, self.last_name, self.email_address)

class Task(models.Model):
	'''
	Task model for the database.

	Fields
		user - ForeignKey - This is a relation to the User database entry under which
			this task belongs.
		subject - string - Descriptor for the task.
		length - float - time in hours anticipated for the task.
		difficulty - integer - rating 1 through 10.
		due_date - datetime
	'''
	user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	subject = models.CharField(max_length = 200)
	length = models.FloatField()
	difficulty = models.IntegerField()
	due_date = models.DateTimeField(null = True)

	def __str__(self):
		'''
		To string function.
		'''
		return "Tasks {}: length-{}, difficulty-{}, due-date-{}".format(self.subject, self.length, self.difficulty, self.due_date)

