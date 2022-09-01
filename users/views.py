from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, get_user_model, password_validation, login, logout
from django.http import HttpResponse
from django.conf import settings

UserModel = get_user_model()

def index(request):
    req_user = request.user
    return render(request, 'users/index.html')

""" User account creation """

def register(request):
    return HttpResponse("Register")