from django.utils import timezone
from django.http.response import StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from account1.models import Customer
from store.models import Certification
from django.contrib.auth.models import User
from django.contrib import auth
import cv2
import threading
import pyzbar.pyzbar as pyzbar

# Create your views here.
def make_qr(request):
    user_id = request.user
    return render(request, 'qr.html',{'user':user_id})

def scan_qr_page(request):
    return render(request,'scan.html')

def scan_qr(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam,str(request.user)),content_type="multipart/x-mixed-replace;boundary=frame")

    except:
        pass

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed,self.frame) = self.video.read()
        threading.Thread(target=self.update,args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()


    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

    def return_frame(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()
            return self.frame;


def gen(camera,user):
    i = 0
    while True:
        qr = camera.return_frame()
        for code in pyzbar.decode(qr):
            my_code = code.data.decode('utf-8')
            print(my_code)
            customers = Customer.objects.all()

            for customer_user_id in customers:
                

                if my_code == str(customer_user_id):
                    print('finish')
                    i=1
                    customer = get_object_or_404(Customer,user_id = str(customer_user_id))
                    customer.point = customer.point + 1
                    customer.count = customer.count + 1
                    customer.save()

                    certification = Certification()
                    certification.storeowner_id = user
                    certification.customer_id = str(customer_user_id)
                    certification.customer_point = 1
                    certification.certification_date = timezone.datetime.now()
                    print('스캔시 certification db 테스트: ',certification)
                    certification.save()
                    # print('customer1 : '+customer1)
                    break
            if i == 1:
                break
        # success, qr = cap.read()
        # for code in pyzbar.decode(qr):
        #     my_code = code.data.decode('utf-8')
        #     print(my_code)
        # cv2.imshow('cam',qr)
        # key = cv2.waitKey(1)
        # if key == 27:
        #     break
        if i == 1:
            redirect('/')
            break
        

        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')