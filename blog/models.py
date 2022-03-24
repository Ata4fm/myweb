
from pickle import TRUE
from django.db import models


class Post(models.Model):
        Title=models.CharField(max_length=100)
        Content=models.TextField()
        counted_view = models.IntegerField(default=0) 
        status = models.BooleanField(default=False)
        created_date=models.DateTimeField(auto_now_add=True)
        updated_date=models.DateTimeField(auto_now=True)
        published_date=models.DateTimeField(null=True)

        def __str__(self):
                return "{} - {}".format(self.Title,self.id)
