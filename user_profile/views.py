
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic.edit import UpdateView, CreateView
from django.views import View
from django.contrib.auth import  logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from .models import User, Quality
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .form import RegisterUserForm, ChangeUserInfoForm
from main.models import Ads

class Basic_v(TemplateView):
    template_name = 'main/index.html'
    

    def get(self, request, *args, **kwargs):
        self.object = User.objects.all()
        self.plugs = Ads.objects.all()
        self.user = request.user
        return super().get(request, *args, **kwargs)
            
    def get_context_data(self, **kwargs):
        us = User.objects.all()
        context = super().get_context_data(**kwargs)
    
        context['publisher'] = self.object
        context['user'] = self.user
        context['plugs'] = self.plugs
        return context

    def get_queryset(self):
        return self.object.all()
    


class PassChange(SuccessMessageMixin,PasswordChangeView, LoginRequiredMixin):
    template_name = 'profile/pass_change.html'
    success_message = 'Пароль пользователя изменен'
    success_url = reverse_lazy('main:login')

class Logining(LoginView):
    template_name = 'profile/login.html'
    

def logoutuser(request):
    logout(request)
    return redirect('user_profile:login')


class RegisterUserView(CreateView):
    model = User
    template_name = 'profile/register_user.html'
    form_class = RegisterUserForm
    redirect_field_name = reverse_lazy('main:main')


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin,
                                              UpdateView):
    model = User
    template_name = 'profile/editprofile.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('user_profile:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)    


class Profile_v(TemplateView):
    template_name = 'profile/main_profile.html'
    model = User
   
    def get(self, request, *args, **kwargs):
        self.object = User.objects.all()
        self.user = request.user
        self.ads = Ads.objects.filter(author=request.user.pk)
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
            

    


    def get_context_data(self, **kwargs):
        us = User.objects.all()
       
        # for i in us:
        #     if i.owner == user:
    
        context = super().get_context_data(**kwargs)
        context['user'] = self.user
        context['publisher'] = self.object
        context['bbs'] = self.ads
        return context
       


