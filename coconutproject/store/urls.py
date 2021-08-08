from django.urls import path
from django.urls.resolvers import URLPattern
from .import views


urlpatterns = [
    path('map',views.map,name = "map"),
    path('store_registration/', views.store_registration, name = "store_registration"),
    path('detail/', views.store_detail, name = "store_detail"),
    path('review/', views.store_review, name = "store_review"),
    path('like/', views.store_like, name = "store_like"),
]