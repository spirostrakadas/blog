from django.db import models
from django.contrib.auth import get_user_model 
import uuid
from datetime import datetime

# Create your models here.]
User=get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(max_length=200,blank=True)
    profile_img=models.ImageField(upload_to='profile_images')
    location= models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images',null=True,blank=True)
    video = models.FileField(upload_to='videos_uploaded',null=True,blank=True)
    caption=models.TextField(max_length=300)
    created_at=models.DateTimeField(default=datetime.now)
    

    def __str__(self):
        return self.user
    