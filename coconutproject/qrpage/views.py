from django.shortcuts import render
from account.models import Customer
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def make_qr(request):
    user_id = request.user
    return render(request, 'qr.html',{'user':user_id})