from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import AccountUser
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserForgetPasswordForm, UserRegisterForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings


class ForgotPasswordView(generic.TemplateView):
    template_name = ""


class LoginView(generic.TemplateView):
    template_name = ""


class RegisterView(generic.TemplateView):
    template_name = ""
