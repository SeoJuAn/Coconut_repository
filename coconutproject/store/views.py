from django.shortcuts import render, redirect
from .models import Store

# Create your views here.


# 지도 생성
def map(request):
    store = Store.objects.all()
    # addresses = []
    # for i in range(len(store)):
    #     addresses.append(store[i].address)
    storeINFO = []
    for i in range(len(store)):
        name_and_address = []
        name_and_address.append(store[i].storename)
        name_and_address.append(store[i].address)

        storeINFO.append(name_and_address)



    # return render(request,'map.html')
    return render(request,'map.html',{'storeINFO':storeINFO})

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
        photo = request.POST['photo']

        store = Store()
        #store.user_id = 
        #store.store_num = 
        store.point = 0
        store.count = 0
        store.review_score = 0
        store.phonenumber = phonenumber
        store.address = address
        store.operationtime = operationtime
        store.menu = menu
        store.category = category
        store.photo = photo
        #store.location = 
        store.pick_count = 0
        store.container_type = container_type
        store.parking = parking
        store.storename = storename
        store.save()
        return redirect('/')

    else:
        return render(request, 'store_registration.html')



