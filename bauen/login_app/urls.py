from login_app import views
from django.urls import path
from .views import login, signup, dashboard

urlpatterns = [
    path('/login/', login, name = 'login'),
    path('/signup/', signup, name = 'signup')
    path('/dashboard/', dashboard, name = 'dashboard'),
]
