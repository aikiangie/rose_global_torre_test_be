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

    def get_queryset(self):
        """
        Optionally restricts the returned tasks to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = UserTasks.objects.all()
        userId = self.request.query_params.get('userId', None)
        if userId is not None:
            queryset = queryset.filter(user=userId)
        return queryset
