from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView,LoginView
urlpatterns = [
    path('register/',SignUp,name="SignUp"),
    path("logout/",LogoutView.as_view(),name="logout" ),
    path('login/',LoginView.as_view(template_name="person/SignIn.html"),name="login")
]
