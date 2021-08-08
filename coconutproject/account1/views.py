from django.shortcuts import render, redirect
from django.contrib.auth.models import User, update_last_login
from django.contrib import auth
from django.utils import timezone
from .models import Customer, StoreOwner, ProductCompany

# Create your views here.

# 사용자가 어떤 카테고리(고객, 가맹점주, 제품제조업체)로 회원가입할지 선택
def signup_choice(request):
    if request.method == "POST":
        choice = request.POST['choice']
        # 사용자가 customer를 선택했다면
        if choice == "customer":
            return render(request,'signup_customer.html')

        # 사용자가 storeowner를 선택했다면
        elif choice == "storeowner":
            return render(request,'signup_storeowner.html')

        # 사용자가 productcompany를 선택했다면
        else :
            return render(request,'signup_productcompany.html')

    else:
        return render(request,'signup_choice.html')

# 고객으로 회원가입
def signup_customer(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        email = request.POST['email']
        name = request.POST['name']
        nickname = request.POST['nickname']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        age = request.POST['age']
        if age == '':
            age = 0
        gender = request.POST['gender']
        photo = request.POST['photo']
        sns = request.POST['sns']
        if User.objects.filter(username = id).exists():
            return render(request, 'signup_customer.html',{'error':"이미 존재하는 사용자입니다."})
        if password == request.POST['passwordCheck']:
            customer = Customer()
            customer.user_id = id
            customer.password = password
            customer.email = email
            customer.user_name = name
            customer.count = 0
            customer.point = 0
            # 나무님!! 이 부분에 customer 객체들(DB 테이블에 있는 애들) 더 추가해주시면 돼요~
            customer.nickname = nickname
            customer.address = address
            customer.phonenumber = phonenumber
            customer.subdate = timezone.datetime.now()
            customer.age = age
            customer.gender = gender
            customer.coupon = 0
            customer.photo = photo
            customer.sns = sns
            customer.save()
            user = User.objects.create_user(
                id, password = password,email=email
            )
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request,'signup_customer.html',{'error':"비밀번호 확인이 일치하지 않습니다."})

    else:
        return render(request,'signup_customer.html')

# 가맹점주로 회원가입
def signup_storeowner(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        email = request.POST['email']
        nickname = request.POST['nickname']
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        sns = request.POST['sns']
        if User.objects.filter(username = id).exists():
            return render(request, 'signup_storeowner.html',{'error':"이미 존재하는 사용자입니다."})
        if password == request.POST['passwordCheck']:
            storeowner = StoreOwner()
            # 나무님!! 이 부분에 StoreOwner 객체들(model.py에 새로 만들고) 새로 추가해주시면 돼요~
            storeowner.user_id = id
            storeowner.password = password
            storeowner.email = email
            storeowner.point = 0
            storeowner.count = 0
            storeowner.nickname = nickname
            storeowner.user_name = name
            storeowner.phonenumber = phonenumber
            storeowner.subdate = timezone.datetime.now()
            storeowner.sns = sns
            storeowner.save()
            user = User.objects.create_user(
                id, password = password,email=email
            )
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request,'signup_storeowner.html',{'error':"비밀번호 확인이 일치하지 않습니다."})

    else:
        return render(request,'signup_storeowner.html')

# 제품제도업체로 회원가입
def signup_productcompany(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        accountnumber = request.POST['accountnumber']
        companyname = request.POST['companyname']
        productcategory = request.POST['productcategory']
        address = request.POST['address']
        operationtime = request.POST['operationtime']
        if User.objects.filter(username = id).exists():
            return render(request, 'signup_productcompany.html',{'error':"이미 존재하는 사용자입니다."})
        if password == request.POST['passwordCheck']:
            productcompany = ProductCompany()
            # 나무님!! 이 부분에 productcompany 객체들(model.py에 새로 만들고) 새로 추가해주시면 돼요~
            productcompany.user_id = id
            productcompany.password = password
            productcompany.email = email
            productcompany.phonenumber = phonenumber
            productcompany.accountnumber = accountnumber
            productcompany.companyname = companyname
            productcompany.productcategory = productcategory
            productcompany.address = address
            productcompany.operationtime = operationtime
            productcompany.save()
            user = User.objects.create_user(
                id, password = password,email=email
            )
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request,'signup_productcompany.html',{'error':"비밀번호 확인이 일치하지 않습니다."})

    else:
        return render(request,'signup_productcompany.html')

def login(request):
    if request.method == "POST":
        id = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username = id, password= password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else :
            return render(request, 'login.html', {'error':"사용자 이름 혹은 패스워드가 일치하지 않음"})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
