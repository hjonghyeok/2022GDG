from django.db import models
from django.conf import settings
# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, null=True)
    mbti = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user