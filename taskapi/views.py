from rest_framework import viewsets

from .serializers import UserSerializer
from .serializers import UserTasksSerializer
from .models import User
from .models import UserTasks


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer


class UserTasksViewSet(viewsets.ModelViewSet):
    queryset = UserTasks.objects.all().order_by('description')
    serializer_class = UserTasksSerializer
