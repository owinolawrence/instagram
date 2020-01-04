# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile, Comments,Image


# Register your models here.
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Image)