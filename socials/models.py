# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 30)
    

    def __str__(self):
        return self.name


    @classmethod
    def search_by_name(cls,search_term):
        socials = cls.objects.filter(title__icontains=search_term)
        return socials
