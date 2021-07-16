from django.urls import path
from django.urls.resolvers import URLPattern
from .import views


urlpatterns = [
    path('map',views.map,name = "map"),
    path('store_registration/', views.store_registration, name = "store_registration"),
]