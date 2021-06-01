from login_app import views
from django.urls import path

urlpatterns = [
    path('', views.login, name = 'login')
]
