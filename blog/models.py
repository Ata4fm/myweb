
from email.policy import default
from pickle import TRUE
from unicodedata import category
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Category(models.Model):
        name = models.CharField(max_length=255)

        def __str__(self):
                return self.name


class Post(models.Model):
        image = models.ImageField(upload_to = 'blog/' , default='blog/default.jpg')
        author = models.ForeignKey(User ,on_delete=models.SET_NULL,null=True)
        Title=models.CharField(max_length=100)
        Content=models.TextField()
        tags = TaggableManager()
        counted_view = models.IntegerField(default=0)
        category = models.ManyToManyField(Category)
        status = models.BooleanField(default=False)
        created_date=models.DateTimeField(auto_now_add=True)
        updated_date=models.DateTimeField(auto_now=True)
        published_date=models.DateTimeField(null=True)

        class Meta:
                ordering = ['-created_date'] 

        def snippets(self):
                return self.Content


        def __str__(self):
                return "{} - {}".format(self.Title,self.id)


        def get_absolute_url(self):
                return reverse('blog:single', kwargs={'pid':self.id}) 

