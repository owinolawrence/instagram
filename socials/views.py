# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    return render(request, "index.html")


def search_results(request):

    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_users = User.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"articles": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})