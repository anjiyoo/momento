from django.db import models
from apps.travel.models import County
from apps.userinfo.models import User

# 여행일정
class TripRecommend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # 유저 모델 외부키
    city_name = models.ForeignKey(County, on_delete=models.SET_NULL, null=True)  # 도시 외부키 참조
    rec_who = models.CharField(max_length=20,default='혼자')  # 동행자 정보
    rec_start_date = models.DateField()  # 여행기간(출발)
    rec_end_date = models.DateField()  # 여행기간(도착)
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일

    def str(self):
        return self.city_name.name


# 여행스타일
class TripStyleRecommend(models.Model):
    rec_trip = models.ForeignKey(TripRecommend,on_delete=models.CASCADE)  # 여행일정 외부키 참조
    rec_style = models.CharField(max_length=30)  # 여행스타일

    def str(self):
        return self.rec_style


# 관광지
class CitySpotRecommend(models.Model):
    city_name = models.ForeignKey(County, on_delete=models.CASCADE, related_name='rec_tour_spots')  # 도시 외부키 참조
    rec_title = models.CharField(max_length=50)  # 관광지
    rec_address = models.TextField()  # 주소
    rec_img = models.ImageField(upload_to='planrecommend/img', blank=True, null=True)  # 이미지
    rec_content_id = models.IntegerField(unique=True)  # 관광지 고유 id
    rec_map_x = models.FloatField(default=0.0)  # 경도
    rec_map_y = models.FloatField(default=0.0)  # 위도

    def str(self):
        return self.rec_title


# 날짜별 여행일정
class DayPlanRecommend(models.Model):
    rec_trip = models.ForeignKey(TripRecommend,on_delete=models.CASCADE)  # 여행일정 외부키 참조
    rec_spot = models.ForeignKey(CitySpotRecommend,on_delete=models.CASCADE)  # 관광지 외부키 참조
    day = models.DateField()  # 일자

    def str(self):
        return self.day
