#from coconutproject.account.models import Customer
from collections import namedtuple
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Photo, Photo_review, Store, Review
from account1.models import Customer
from random import *
# Create your views here.


# 지도 생성
def map(request):
    store = Store.objects.all()
    photo = Photo.objects.all()
    review = Review.objects.all()
    photo_review = Photo_review.objects.all()
    # addresses = []
    # for i in range(len(store)):
    #     addresses.append(store[i].address)
    # print(photo[0].store)
    # print(photo[0].image.url)
    storeINFO = []
    for i in range(len(store)):
        name_and_address = []
        name_and_address.append(store[i].storename)
        name_and_address.append(store[i].address)
        name_and_address.append(store[i].review_score)
        name_and_address.append(store[i].pick_count)
        name_and_address.append(store[i].phonenumber)
        name_and_address.append(store[i].operationtime)
        name_and_address.append(store[i].category)
        name_and_address.append(store[i].menu)
        name_and_address.append(store[i].container_type)
        name_and_address.append(store[i].parking)

        for j in range(len(photo)):
            #print(str(photo[j].store))
            if str(photo[j].store) == store[i].storename :
                print('들어옴')
                name_and_address.append(photo[j].image.url)
        

        #print(name_and_address)
        storeINFO.append(name_and_address)

    review_list = [] 
    for i in range(len(review)):
        content = []
        content.append('review')
        content.append(review[i].customer_id)
        content.append(review[i].storeowner_id)
        content.append(review[i].product_review_score)
        content.append(review[i].takeout_review_score)
        content.append(review[i].write_date)
        content.append(review[i].content)

        for j in range(len(photo_review)):
            #print(photo_review[j].review.review_num)
            if photo_review[j].review.review_num == review[i].review_num:
                 content.append(photo_review[j].image.url)

        review_list.append(content)

    review_list.append('review')
    storeINFO.append(review_list)
    #storeINFO.append(photo[0].image.url)


    # return render(request,'map.html')
    return render(request,'map.html',{'storeINFO':storeINFO})
    #return render(request,'map_search.html',{'storeINFO':storeINFO})

#가맹점 등록
def store_registration(request):
    if request.method == "POST":
        storename = request.POST['storename']
        address = request.POST['address']
        phonenumber = request.POST['phonenumber']
        category = request.POST['category']
        operationtime = request.POST['operationtime']
        menu = request.POST['menu']
        container_type = request.POST['container_type']
        parking = request.POST['parking']
        #photo = request.POST['photo']

        store = Store()
        store.user_id = request.user
        #store.store_num = 
        store.point = 0
        store.count = 0
        store.review_score = 0
        store.phonenumber = phonenumber
        store.address = address
        store.operationtime = operationtime
        store.menu = menu
        store.category = category
        #store.photo = photo
        #store.location = 
        store.pick_count = 0
        store.container_type = container_type
        store.parking = parking
        store.storename = storename
        store.save()
        for img in request.FILES.getlist('photo'):
            photo = Photo()
            photo.store = store
            photo.image = img
            photo.save()
        return redirect('/')

    else:
        return render(request, 'store_registration.html')



def store_detail(request):
    print(request.method)
    return render(request,'detail.html',{'test':'test'})


num = 1

def store_review(request):
    if request.method == "POST":
        global num
        random_num1 = uniform(1.0,1000.0)
        random_num2 = uniform(1.0,1000.0)
        random_num = random_num1 * random_num2
        #store_num = request.POST['store_num']
        #storeowner_id = request.POST['storeowner_id']
        content = request.POST['content']
        
        #별점을 안줬을 때 0으로 처리
        try:
            product_review_score = request.POST['product_review_score']
        except:
            product_review_score = 0

        try:
            takeout_review_score = request.POST['takeout_review_score']
        except:
            takeout_review_score = 0
        #photo = request.POST['photo']
        #review_num = request.POST['review_num']

        review = Review()
        review.customer_id = request.user
        #review.store_num = store_num
        review.storeowner_id = request.POST['storename']

        review.content = content
        review.product_review_score = product_review_score
        review.takeout_review_score = takeout_review_score
        review.write_date = timezone.datetime.now()
        #review.photo = photo
        review.review_num = random_num
        num = num + 1
        review.save()
        for img in request.FILES.getlist('photo'):
            photo_review = Photo_review()
            photo_review.review = review
            photo_review.image = img
            photo_review.save()
        return redirect('/')

    else:
        return render(request,'review.html')


def store_like(request):
    if request.method == "POST":
        customers = Customer.objects.all()
        storeid = request.POST['storeid']
        print(storeid)
        #customer.likestore = customer.likestore + "," +str(storeid)
        for customer in customers:
            if str(customer) == str(request.user):
                print("zmzm emdjdha")
                customer.likestore = str(customer.likestore) + "," + str(storeid)
                print(customer.likestore)
                customer.save()
        
        return redirect('/')

    else:
        return render(request,'review.html')