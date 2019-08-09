from rest_framework import serializers

from .models import User
from .models import UserTasks


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'username')


class UserTasksSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only=True)

        class Meta:
            model = UserTasks
            fields = ('id', 'description', 'state', 'user')
