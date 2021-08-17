from django.core import paginator
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Community, Photo
from account1.models import Customer, StoreOwner
from django.core.paginator import Paginator

# Create your views here.
def commu_main(request):
    communitys = Community.objects
    community_list = Community.objects.all()
    paginator = Paginator(community_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'commu_main.html',{'communitys':communitys,'posts':posts})

def commu_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        writer = str(request.user)
        date = timezone.datetime.now()
        
        community = Community()

        community.title = title
        community.content = content
        community.writer = writer
        community.subdate = date
        community.save()

        for img in request.FILES.getlist('photo'):
            photo = Photo()
            photo.community = community
            photo.image = img
            photo.save()
            
        return redirect('/')
    else:
        return render(request,'commu_create.html')

def commu_detail(request, community_id):
    community_detail = Community.objects.get(id = community_id)
    photo = Photo.objects.all()
    photos = []

    for i in range(len(photo)):
            #print(str(photo[j].store))
            if str(photo[i].community.id) == str(community_id) :
                print(photo[i].image.url)
                photos.append(photo[i].image.url)

    return render(request,'commu_detail.html',{'community':community_detail, 'photos':photos})

def commu_like(request):
    if request.method == "POST":
        customers = Customer.objects.all()
        storeowners = StoreOwner.objects.all()
        communityid = request.POST['communityid']
        print(communityid)
        #customer.likestore = customer.likestore + "," +str(storeid)
        for customer in customers:
            if str(customer) == str(request.user):
                customer.likecommunity = str(customer.likecommunity) + "," + str(communityid)
                print(customer.likecommunity)
                customer.save()
        for storeowner in storeowners:
            if str(storeowner) == str(request.user):
                storeowner.likecommunity = str(storeowner.likecommunity) + "," + str(communityid)
                print(storeowner.likecommunity)
                storeowner.save()

        
        return redirect('/')

    else:
        return render(request,'commu_detail.html')