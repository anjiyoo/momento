from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('list/', ListAccommodations.as_view(), name='list_domestic_accommodations'),
    path('review/list/', ListReviews.as_view(), name='list_reviews'),
    path('detail/<int:pk>/', AccomodationDetailView.as_view(), name='accommodation_detail'),
    path('detail/<int:accommodation_pk>/room/<int:room_pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('detail/<int:pk>/map/', my_view, name='map'),
    path('reservation/<int:accommodation_pk>/room/<int:room_pk>/', CreateReservation.as_view(), name='create_reservation'),
    # path('detail/<int:pk>/save/', SaveAccommodationView.as_view(), name='save_accommodation'),
    # path('detail/<int:pk>/unsave/', UnsaveAccommodationView.as_view(), name='unsave_accommodation'),
    path('detail/<int:pk>/create_review/', CreateReview.as_view(), name='create_review'),
    path('detail/<int:accommodation_pk>/review/<int:review_pk>/', ReviewDetailView.as_view(), name='review_detail'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
