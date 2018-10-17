from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class FormModel(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    entry = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username