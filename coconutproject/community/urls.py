from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns = [
    path('main/', views.commu_main, name = "commu_main"),
    path('create/', views.commu_create, name = "commu_create"),
    path('<int:community_id>/', views.commu_detail, name = "commu_detail"),
    path('likecommunity/', views.commu_like, name = "commu_like"),
]
