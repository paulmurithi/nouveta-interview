from django.shortcuts import render, redirect
from django.views import View
from .models import Package
from .forms import Register
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings

class Register(View):
    template = "registration/register.html"
    form_class = Register
    title = 'register'

    def get(self, request):
        form =self.form_class(None)
        return render(request, self.template, { 'form' : form })
        
    def post(self, request):
        form = self.form(request.POST)
        print('not validated')
        
        if form.is_valid():
            print('validated')
            email = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # check if user has an account
            user_exists = User.objects.filter(username=username).exists()
            if user_exists:
                context = {
                    'form' : self.form(request.POST),
                    'errors': 'staff already registered'
                }
                return render(request, self.template, context)
            
            # register new user
            register_user = User.objects.create_user(username, email, password)
            register_user.save()
            
            
            # messages.success(request,'Account has been successfully created')
            return redirect('login')
            


class WebsiteIndex(View):
    login_url = settings.LOGIN_URL
    template = "rejco/index.html"

    def get(self, request):
        return render(request, self.template, {})

class CustomerIndex(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/customer/index.html"

    #test if the user customer
    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def get(self, request):
        user = self.request.user
        packages = Package.objects.filter(owner = user)
        print(packages)
        return render(request, self.template, {'packages':packages})

class AdminIndex(LoginRequiredMixin, UserPassesTestMixin,View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    #test if the user admin
    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def get(self, request):
        packages = Package.objects.all()
        print(packages)
        return render(request, self.template, {'packages':packages})

class UpdateDispatchStatus(LoginRequiredMixin, UserPassesTestMixin,View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    #test if the user admin
    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def post(self, request, packageId):
        package = Package.objects.get(id=packageId)
        dispatch = package.dispatch
        package.dispatch = not dispatch
        package.save()
        return render(request, self.template )
        
class UpdateArrivalStatus(LoginRequiredMixin, UserPassesTestMixin,View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    #test if the user admin
    def test_func(self):
        user = self.request.user
        return Student.objects.filter(adm_no=user).exists()

    def post(self, request, packageId):
        package = Package.objects.get(id=packageId)
        dispatch = package.arrived
        package.dispatch = not arrived
        package.save()
        return render(request, self.template )
        

