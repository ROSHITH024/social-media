from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/')
    about=models.CharField(max_length=250 ,null=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profile_pic=models.ImageField(upload_to='proimages',null=True)
    place=models.CharField(max_length=100,null=True)
    bio=models.CharField(max_length=250 ,null=True)
    

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",null=True,blank=True)
    created_date=models.DateField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name="like")
    savers = models.ManyToManyField(User,blank=True , related_name='saved')
    comment_count = models.IntegerField(default=0)
    @property
    def likes(self):
        return self.like.all().count()
    @property
    def post_comments(self):
        qs=self.comment_set.all()
        return qs

    # def __str__(self):
    #     return self.user

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.comment

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    followers = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='following',null=True)
    

