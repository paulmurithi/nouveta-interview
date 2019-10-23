from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "rejco"
urlpatterns = [
    path('register', views.Register.as_view(), name='register'),
    path('administrator/', views.AdminIndex.as_view(), name='admin'),
    path('administrator/dispatch/<slug:id>/', views.UpdateDispatchStatus.as_view(), name='dispatch'),
    path('administrator/arrived/<slug:id>/', views.UpdateArrivalStatus.as_view(), name='arrived'),
    path('customer/', views.CustomerIndex.as_view(), name='customer'),
    path('customer/notifications/', views.Notifications.as_view(), name='notifications'),
    path('customer/notifications/<slug:id>/', views.NotificationDetail.as_view(), name='notification_detail'),
    # path('customer/notifications/<slug:id>/read', views.ReadNotification.as_view(), name='notification_read'),
    path('', views.WebsiteIndex.as_view(), name='index'),
]