from django.http.response import StreamingHttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from account.models import Customer
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
        return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")

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


def gen(camera):
    i = 0
    while True:
        qr = camera.return_frame()
        for code in pyzbar.decode(qr):
            my_code = code.data.decode('utf-8')
            print(my_code)
            if my_code == 'customer1':
                print('finish')
                i=1
                customer = get_object_or_404(Customer,user_id = 'customer1')
                customer.point = customer.point + 10
                customer.count = customer.count + 1
                customer.save()
                # print('customer1 : '+customer1)
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
            redirect('home')
            break
        

        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')