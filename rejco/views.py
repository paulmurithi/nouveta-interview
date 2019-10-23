from django.shortcuts import render, redirect
from django.views import View
from .models import Package, Notification
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
        form = self.form_class(request.POST)
        print('not validated')
        
        if form.is_valid():
            print('validated')
            username = form.cleaned_data['username']
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
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('rejco:admin')
            else:
                return redirect('rejco:customer')
        else:
            return render(request, self.template, {})

class CustomerIndex(LoginRequiredMixin,  View):
    login_url = settings.LOGIN_URL
    template = "rejco/customer/index.html"

    def get(self, request):
        user = self.request.user
        packages = Package.objects.filter(owner = user)
        print(packages)
        notifications = Notification.objects.filter(user = user, viewed=False)
        return render(request, self.template, {'packages':packages, 'notifications': notifications})

class AdminIndex(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    def get(self, request):
        packages = Package.objects.all()
        print(packages)
        return render(request, self.template, {'packages':packages})

class UpdateDispatchStatus(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    def get(self, request, id):
        package = Package.objects.get(id=id)
        dispatched = package.dispatched
        package.dispatched = not dispatched
        package.save()
        return redirect('rejco:admin')
        
class UpdateArrivalStatus(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/admin/index.html"

    def get(self, request, id):
        package = Package.objects.get(id=id)
        arrived = package.arrived
        package.arrived = not arrived
        package.save()
        return redirect('rejco:admin')
        
class Notifications(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/customer/notifications.html"

    def get(self, request):
        user = self.request.user
        notifications = Notification.objects.filter(user = user, viewed=False)
        print(notifications)
        return render(request, self.template, {'notifications': notifications} )

class NotificationDetail(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    template = "rejco/customer/notification_detail.html"

    def get(self, request, id):
        notification = Notification.objects.get(id = id)
        return render(request, self.template, {'notification': notification} )

    def post(self, request, id):
        notification = Notification.objects.get(id=id)
        notification.viewed = True
        notification.save()
        return redirect('rejco:notifications')
