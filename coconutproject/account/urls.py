from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('signup/', views.signup_choice, name = "signup_choice"),
    path('signup_customer/', views.signup_customer, name = "signup_customer"),
    path('signup_productcompany/', views.signup_productcompany, name = "signup_productcompany"),
    path('signup_storeowner/', views.signup_storeowner, name = "signup_storeowner"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
]
