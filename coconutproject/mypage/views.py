from django.shortcuts import render, redirect
from store.models import Photo_review, Review
from account1.models import Customer, StoreOwner
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

    return render(request,'mypoint.html',{'point':point})

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
    # try:
    #     customer = Customer.objects.filter(user_id=str(request.user))
    #     likestores = str(customer[0].likestore).split(',')
    #     likestores = likestores[1:]
    #     temp = set(likestores)
    #     likestores = list(temp)
    #     print(likestores)
    # except:
    #     likestores = []
    return render(request,'mypage_wish_community.html')