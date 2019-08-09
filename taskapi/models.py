from django.db import models


class User(models.Model):
    name = models.CharField(max_length=300, blank=False)
    username = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class UserTasks(models.Model):
    TASK_STATES = (
        ('TO_DO', 'To do'),
        ('DONE', 'Done'),
    )
    description = models.CharField(max_length=300, blank=False)
    state = models.CharField(max_length=300, blank=False, choices=TASK_STATES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
