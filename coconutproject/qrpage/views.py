from django.shortcuts import render
from .models import Qrpage
from account.models import Customer
from django.contrib.auth.models import User
from django.contrib import auth
from account.views import signup_customer

from django.http import HttpResponse
import qrcode
from io import BytesIO

# Create your views here.
# def make_qr(request):
#     name = 'rio'

#     obj = Qrpage.objects.get(id=1)

#     context = {
#         'name' : name,
#         'obj' : obj,
#     }
#     print(context)

#     return render(request, 'qr.html',context)

def make_qr(request):
    user_id = request.user
    print('dmdmdkddk')
    return render(request, 'qr.html',{'user':user_id})