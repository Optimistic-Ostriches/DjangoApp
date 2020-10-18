from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
#.....com/api/users/
router.register(r'users', views.UserViewSet)
#.....com/api/user/2/tasks/

urlpatterns = [
	# User endpoints are constructed via the REST Framework ViewSet
	# 	schema.
    path('', include(router.urls)),
    # Tasks endpoints require database key for relevant user
    path('users/<int:pk>/tasks/', views.tasks_view, name='tasks_view'),
    # API Authorization for REST Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]