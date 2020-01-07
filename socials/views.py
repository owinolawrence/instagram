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


# @login_required
def profile(request):
  current_user = request.user
  profile = Profile.objects.get(user=request.user)
  
  images = Image.objects.filter(uploader_profile_id = current_user.id)
  post =images.count()
  
  return render(request,'profile.html',{"images":images, "post":post,'profile':profile})

class createimage(LoginRequiredMixin, CreateView):
    
    model = Image
    fields =['image','caption'] 

    def form_valid(self,form):
        form.instance.uploader_profile = self.request.user
        return super().form_valid(form)

# @login_required
def comments(request,image_id):
  Comments_form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    Comments_form = CommentForm(request.POST)
    if Comments_form.is_valid():
      comment = Comments_form.save(commit = False)
      profile = Profile.objects.get(user=request.user)
      comment.author = profile
      
      comment.imagecomment = image
      comment.save() 
  return redirect('home')


