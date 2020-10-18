from django.contrib import admin


from .models import User, Task
# Register User model to admin web console
admin.site.register(User)
# Register Task model to admin web console
admin.site.register(Task)