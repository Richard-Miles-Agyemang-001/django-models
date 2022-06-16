from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField("posted here ")
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
def __str__(self):
		return self.title
Created_date = Post = models.DateTimeField(auto_now=False, auto_now_add=False)
Published_date = Post = models.DateTimeField(auto_now=False, auto_now_add=False)
    