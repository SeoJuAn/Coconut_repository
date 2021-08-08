from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mypoint/', views.mypoint, name = "mypoint"),
    path('review/', views.mypageReview, name = "mypageReview"),
    path('orderhistory/', views.orderHistory, name = "orderHistory"),
    path('wishstore/', views.wishstore, name = "wishstore"),
    path('changeprivacy/', views.changeprivacy, name = "changeprivacy"),
]
