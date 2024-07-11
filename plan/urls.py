from django.urls import path
from . import views
app_name= 'plan'
urlpatterns = [
    path('city/',views.CityList.as_view(),name='city'),
    path('days/',views.days,name='days'),
    path('test/',views.get_tour_data),
    path('day_plan/<int:region>/<int:cigungu1>/<int:cigungu2>/<int:cigungu3>',views.day_plan,name='day_plan')
]