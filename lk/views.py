from typing import Any
from django.http.request import HttpRequest as HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, View, TemplateView, UpdateView, CreateView
from lk.models import User
from django.http import Http404
from lk.const import *
from vacations.const import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from vacations.models import VacationRequest
from .forms import AddEmployerForm
from django.urls import reverse_lazy

def get_user_by_id(id,):
    try:
        user = User.objects.get(pk=id)
        return user
    except User.DoesNotExist:
        return None
    
# Create your views here.
class LkView(TemplateView):
    template_name = 'lk.html'
    user = None
    employers = None
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login_user')
        return super().dispatch(request, *args, **kwargs)
        
        
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = get_user_by_id(request.user.pk)
        if self.user and self.user.user_type == USER_TYPE_BOSS:
            self.employers = User.objects.filter(user_boss=request.user.pk)           
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(LkView, self).get_context_data(**kwargs)
        if self.employers:
            context.update({
                'employers': self.employers
            })
        context.update({
            'user': self.user,
        })
        return context

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('lk')
            messages.error(request, "Invalid login/password")
            return redirect('login_user')
        else:
            return render(request, 'login.html', {'login': 'login'})
    return redirect('lk')


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully loggedout")
    return redirect('login_user')

class VacationRequestListView(ListView):
    
    http_method_names = ['get']
    context_object_name = 'vacations'
    model = VacationRequest
    template_name = 'vacation_request_list.html'

    def get_queryset(self):
        queryset = super(VacationRequestListView, self).get_queryset()
        queryset = VacationRequest.objects.filter(user=self.request.user).order_by('start_date')
        return queryset
    

class BossVacationRequestListView(VacationRequestListView):
    
    http_method_names = ['get', 'post']
    template_name = 'boss_vacation_request_list.html'
    

    def get_queryset(self):
        queryset = super(BossVacationRequestListView, self).get_queryset()
        users = User.objects.filter(user_boss=self.request.user)
        queryset = VacationRequest.objects.filter(user__in=users, status=WAITING).order_by('pk','start_date')
        return queryset

class CreateEmployerView(CreateView):
    model = User
    form_class = AddEmployerForm
    template_name = 'add_employer.html'
    success_url = reverse_lazy('lk')

    def dispatch(self, *args, **kwargs):
        if  self.request.user.user_type == USER_TYPE_BOSS:
            return super(CreateEmployerView, self).dispatch(*args, **kwargs) 

        return redirect('lk')