from rest_framework import serializers

from .models import User
from .models import UserTasks


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'username')


class UserTasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserTasks
        fields = ('id', 'description', 'state', 'user')
