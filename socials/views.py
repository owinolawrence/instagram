from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import (
    CreateView,
    UpdateView,
)
from . import forms
from .forms import RegisterForm , ImageForm,CommentForm,UpdateUser,UpdateProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Image,Profile,Comments
from django.http import HttpResponse


def signup(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            input_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=input_password)
            login(request, user)
            messages.success(request, f'Account created for {username}')
            return redirect('home')
        

    else :
        form = RegisterForm()
    return render(request, 'auth/signup.html', {'form':form})

# @login_required
def home(request):
    current_user = request.user
    comment_form = CommentForm()
    images = Image.showall_images()
    comment = Comments.objects.all()
   
    return render(request, 'index.html', {'comment_form':comment_form,'images':images,'current_user':current_user,'comment':comment})


