from django.db import models
#import user method for django
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


class Profile(models.Model):
    '''
    describe the account owner using text
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_pic = models.ImageField(default = 'default.jpg',upload_to = 'ProfilePIcture/')
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    


