from django.shortcuts import render, redirect, get_object_or_404
from store.models import Store, Photo_review, Review
from account1.models import Customer, StoreOwner
from store.models import Certification
from community.models import Community
from django.contrib.auth.models import User, update_last_login
from django.contrib import auth

# Create your views here.
def mypage(request):
    return render(request,'mypage.html')

def mypoint(request):
    customer = Customer.objects.all()
    point = 0
    for i in range(len(customer)):
        if(str(customer[i])==str(request.user)):
            point = customer[i].point

    certification = Certification.objects.all()
    certification_list = [point]
    #certification_list.append(point)
    print('certification list: ',certification_list)
    for i in range(len(certification)):
        if(str(certification[i].customer_id) == str(request.user)):
            try :
                list = []
                list.append(certification[i].customer_point)
                list.append(certification[i].certification_date)
                store = Store.objects.filter(user_id=str(certification[i].storeowner_id))
                list.append(str(store[0]))  #.storename이 없다고 오류가 뜸
                certification_list.append(list)
                    #certification_list=[누적포인트, [고객 포인트,날짜,가게], ...]
            except:
                certification_list = [point]

    print('certification list: ',certification_list)
    return render(request,'mypoint.html',{'certification_list':certification_list})

def mypageReview(request):
    print(request.user)
    review = Review.objects.all()
    reviews = []
    for i in range(len(review)):
        if(str(review[i].customer_id)==str(request.user)):
            contents = []
            print(review[i].content)
            print(review[i].storeowner_id)
            contents.append(review[i].storeowner_id)
            contents.append(review[i].write_date)
            contents.append(review[i].content)
            contents.append(review[i].review_num)
            reviews.append(contents)
            
        #reviews.append(contents)
        
    return render(request,'mypage_review.html',{'reviews':reviews})

def orderHistory(request):
    return render(request,'mypage_order_history.html')

def wishstore(request):
    try:
        customer = Customer.objects.filter(user_id=str(request.user))
        likestores = str(customer[0].likestore).split(',')
        likestores = likestores[1:]
        temp = set(likestores)
        likestores = list(temp)
        print(likestores)
    except:
        likestores = []
    return render(request,'mypage_wish_store.html',{'likestores':likestores})

def changeprivacy(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        nickname = request.POST['nickname']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        age = request.POST['age']
        gender = request.POST['gender']
        photo = request.POST['photo']
        sns = request.POST['sns']
        if age == '':
            age = 0
        try:
            customer = Customer.objects.get(user_id = str(request.user))
            customer.email = email
            customer.user_name = name
            customer.nickname = nickname
            customer.address = address
            customer.phonenumber = phonenumber
            customer.age = age
            customer.gender = gender
            customer.photo = photo
            customer.sns = sns
            customer.save()

        except:
            try:
                storeowner = StoreOwner.objects.get(user_id = str(request.user))
                storeowner.email = email
                storeowner.user_name = name
                storeowner.nickname = nickname
                storeowner.phonenumber = phonenumber
                storeowner.save()
            except:
                pass
            
            
        return redirect('/')

        
    else:
        return render(request,'mypage_privacy.html')

def mycommunity(request):

    community = Community.objects.all()
    communitys = []
    for i in range(len(community)):
        if(str(community[i].writer)==str(request.user)):
            contents = []
            contents.append(community[i].writer)
            contents.append(community[i].title)
            contents.append(community[i].content)
            contents.append(community[i].subdate)
            communitys.append(contents)
            


    return render(request,'mypage_mycommunity.html',{'communitys':communitys})

def wishcommunity(request):
    try:
        customer = Customer.objects.filter(user_id=str(request.user))
        likecommunitys = str(customer[0].likecommunity).split(',')
        likecommunitys = likecommunitys[1:]
        temp = set(likecommunitys)
        likecommunitys = list(temp)
        print(likecommunitys)
    except:

        try :
            storeowner = StoreOwner.objects.filter(user_id=str(request.user))
            likecommunitys = str(storeowner[0].likecommunity).split(',')
            likecommunitys = likecommunitys[1:]
            temp = set(likecommunitys)
            likecommunitys = list(temp)
            print(likecommunitys)
        except:
            likecommunitys = []

    communitys = []
    for i in range(len(likecommunitys)):
        try:
            community = Community.objects.get(id = int(likecommunitys[i]))
            contents = []
            contents.append(community.writer)
            contents.append(community.title)
            contents.append(community.content)
            contents.append(community.subdate)
            communitys.append(contents)
            print('에러 안남')
        except:
            print('에러 남')
    print(communitys)
    return render(request,'mypage_wish_community.html',{'communitys':communitys})

def purchasecoupon(request):
    if request.method == "POST":
        customer = get_object_or_404(Customer,user_id = str(request.user))
        choice = request.POST['choice']
        # 사용자가 customer를 선택했다면
        if choice == "5":
            print(choice)
            customer.coupon += "5,"
            customer.point -= 5
            customer.save()

        # 사용자가 storeowner를 선택했다면
        elif choice == "10":
            print(choice)
            customer.coupon += "10,"
            customer.point -= 10
            customer.save()

        elif choice == "15":
            print(choice)
            customer.coupon += "15,"
            customer.point -= 15
            customer.save()

        elif choice == "20":
            print(choice)
            customer.coupon += "20,"
            customer.point -= 20
            customer.save()

        customer = get_object_or_404(Customer,user_id = str(request.user))
        coupon = customer.coupon.split(',')
        return render(request,'mypage_mycoupon.html',{'coupon':coupon})

    else:
        return render(request,'mypage_purchase_coupon.html')
    

def mycoupon(request):
    customer = get_object_or_404(Customer,user_id = str(request.user))
    coupon = customer.coupon.split(',')
    return render(request, 'mypage_mycoupon.html',{'coupon':coupon})