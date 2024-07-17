from django.urls import path
from .views import *

app_name = 'planrecommend'

urlpatterns = [
    path('', SelectCityListView.as_view(), name='select_city'),

]