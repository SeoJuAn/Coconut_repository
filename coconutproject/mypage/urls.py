from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('mypoint/', views.mypoint, name = "mypoint"),
    path('review/', views.mypageReview, name = "mypageReview"),
    path('orderhistory/', views.orderHistory, name = "orderHistory"),
    path('wishstore/', views.wishstore, name = "wishstore"),
    path('changeprivacy/', views.changeprivacy, name = "changeprivacy"),
    path('mycommunity/', views.mycommunity, name = "mycommunity"),
    path('wishcommunity/', views.wishcommunity, name = "wishcommunity"),
    path('purchasecoupon/', views.purchasecoupon, name = "purchasecoupon"),
    path('mycoupon/', views.mycoupon, name = "mycoupon"),
]
