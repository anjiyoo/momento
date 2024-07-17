from django.urls import path
from . import views

app_name = 'planrecommend'

urlpatterns = [
    path('', views.planrecommend_main, name='planrecommend_main'),

]