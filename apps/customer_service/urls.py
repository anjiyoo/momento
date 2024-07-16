from django.urls import path
from .views import InquiryCreateView,InquiryListView,InquiryDetailView

app_name='customer_service'

urlpatterns = [
    path('inquiry/create/', InquiryCreateView.as_view(), name='inquiry_create'),
    path('',InquiryListView.as_view(),name='customer_service'),
    path('inquiry/<uuid:pk>/', InquiryDetailView.as_view(), name='post_detail'),
]