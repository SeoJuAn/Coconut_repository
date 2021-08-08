from django.core import paginator
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Community
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
            
        return redirect('/')
    else:
        return render(request,'commu_create.html')

def commu_detail(request, community_id):
    community_detail = Community.objects.get(id = community_id)
    return render(request,'commu_detail.html',{'community':community_detail})