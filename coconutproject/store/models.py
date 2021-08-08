from django.db import models

# Create your models here.
# 가맹점
class Store(models.Model): 
    user_id = models.CharField(max_length=200, default='')
    store_num = models.IntegerField(default=0)  # 가게(등록)번호 
    point = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    review_score = models.FloatField(default=0)
    phonenumber = models.CharField(max_length=200, default='')  # 전화번호
    address = models.CharField(max_length=200, default='')  # 주소
    operationtime = models.CharField(max_length=200, default='')
    menu = models.CharField(max_length=200, default='')
    category = models.CharField(max_length=200, default='')
    #photo = models.ImageField(upload_to='images/',blank=True,null=True)
    location = models.CharField(max_length=200, default='') # 위치(위도/경도) ->맵 표시용
    pick_count = models.IntegerField(default=0)
    container_type = models.CharField(max_length=200, default='')
    parking = models.CharField(max_length=200, default='')
    storename = models.CharField(max_length=200, default='')    ## 가게이름과 회원가입시 user_name은 다른 거겠죠..?
    def __str__(self):
        return self.storename
class Photo(models.Model):
    store = models.ForeignKey(Store,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

# 인증
class Certification(models.Model):
    storeowner_id = models.CharField(max_length=200, default='')
    customer_id = models.CharField(max_length=200, default='')
    customer_count = models.IntegerField(default=0)
    customer_point = models.IntegerField(default=0)
    storeowner_count = models.IntegerField(default=0)
    storeowner_point = models.IntegerField(default=0)
    ## count, point는 storeowner_~, customer_~로 바뀔 수 있음!
    certification_date = models.CharField(max_length=200, default='')

# 가맹점 리뷰
class Review(models.Model):
    customer_id = models.CharField(max_length=200, default='')
    store_num = models.IntegerField(default=0)
    storeowner_id = models.CharField(max_length=200, default='')
    content = models.TextField(max_length=200, default='')  ## vs CharField??
    product_review_score = models.FloatField(default=0)
    takeout_review_score = models.FloatField(default=0)
    write_date = models.CharField(max_length=200, default='')
    photo = models.CharField(max_length=200, default='')
    review_num = models.FloatField(default=0)
    def __str__(self):
        return self.customer_id

class Photo_review(models.Model):
    review = models.ForeignKey(Review,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)