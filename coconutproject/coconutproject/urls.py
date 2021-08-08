"""coconutproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import home.views
import qrpage.views
import mypage.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home,name="home"),
    path('home/',include('home.urls')),
    path('account/',include('account1.urls')),
    path('qrpage/',qrpage.views.make_qr,name="qrpage"),
    path('scan/',qrpage.views.scan_qr,name="scan"),
    path('qr_scan',qrpage.views.scan_qr_page,name = "qr_scan"),
    path('store/',include('store.urls')),
    path('mypage/',include('mypage.urls')),
    path('mypage/',mypage.views.mypage,name="mypage"),
    path('community/',include('community.urls')),
]
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)