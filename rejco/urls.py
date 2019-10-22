from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "rejco"
urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('customer/', views.CustomerIndex.as_view(), name='customer'),
    path('administrator/', views.AdminIndex.as_view(), name='admin'),
    path('administrator/dispatch/<int:id>/', views.UpdateDispatchStatus.as_view(), name='dispatch'),
    path('administrator/arrived/<int:id>/', views.UpdateArrivalStatus.as_view(), name='arrived'),
    path('', views.WebsiteIndex.as_view(), name='index'),
]