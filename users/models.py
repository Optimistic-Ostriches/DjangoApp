from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	email_address = models.CharField(max_length = 200)

	def __str__(self):
		return "{} {} - {}".format(self.first_name, self.last_name, self.email_address)

class Task(models.Model):
	user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	subject = models.CharField(max_length = 200)
	length = models.FloatField()
	difficulty = models.IntegerField()
	due_date = models.DateTimeField(null = True)
