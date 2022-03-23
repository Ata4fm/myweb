
from django.db import models


class Post(models.Model):
        Title=models.CharField(max_length=100)
        Content=models.TextField()