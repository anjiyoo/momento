# views.py
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Accommodation, Reservation, GuestInfo, TransportationInfo, Room, Review, AccommodationImage,  RoomImage, CancellationPolicy
from apps.userinfo.models import User
from .serializers import AccommodationSerializer, ReservationSerializer, ReviewSerializer
from django.template.response import TemplateResponse
from django.shortcuts import render
from django.db.models import Avg
from django.conf import settings  
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from datetime import datetime



# 숙소 조회
class ListAccommodations(APIView):
    def get(self, request):
        accommodations = Accommodation.objects.all()
        serializer = AccommodationSerializer(accommodations, many=True)
        return Response(serializer.data)

# 숙소 상세 페이지 조회
class AccomodationDetailView(APIView):
    def get(self, request, pk):
        user = request.user
        accommodation = Accommodation.objects.get(pk=pk)
        room = Room.objects.filter(accommodation=accommodation)
        reviews = Review.objects.filter(accommodation=accommodation)
        reviews_count = reviews.count()
        likes_count = accommodation.like.count()

        # 출발일을 request에서 가져오기 (예: 'start_date'라는 쿼리 파라미터로 전달)
        start_date_str = request.query_params.get('start_date')
        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        else:
            start_date = datetime.now().date()  # 출발일이 없으면 기본값으로 오늘 날짜 사용

        # 로그인 한 사용자의 리뷰를 가져와서 첫 번째로 뜨게 하기
        user_review = reviews.filter(user=request.user).first() if request.user.is_authenticated else None
        if reviews_count > 0:
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        else:
            average_rating = 0

        # start_date = request.GET.get('start_date')
        # room_prices = RoomPrice.objects.filter(accommodation=accommodation, date=start_date)
    
        
        accommodation_images = AccommodationImage.objects.filter(accommodation=accommodation)  # Accommodation에 연결된 모든 이미지 가져오기
        room_images = RoomImage.objects.filter(room__in=room)

        min_price_room = room.order_by('price').first()
        min_price = min_price_room.price if min_price_room else None
        min_price_room_id = min_price_room.id if min_price_room else None
       
        context = {
            'accommodation': accommodation,
            'room': room,
            'reviews': reviews,
            'user_review': user_review,
            'MEDIA_URL': settings.MEDIA_URL,
            'images': accommodation_images,
            'room_images': room_images,
            'reviews_count': reviews_count,
            'likes_count': likes_count,
            'average_rating': average_rating,
            'min_price': min_price,
            'min_price_room_id': min_price_room_id,
            # "liked": liked,
        }
        
        return render(request, 'accommodation/accommodation_detail.html', context)
    
        
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
class CreateReservation(APIView):
    def get(self, request, accommodation_pk, room_pk):
        # user = request.user
        accommodation = Accommodation.objects.get(pk=accommodation_pk)
        accommodation_images = AccommodationImage.objects.filter(accommodation=accommodation) 
        cancellationpolicy = CancellationPolicy.objects.first()
        
        room = Room.objects.get(pk=room_pk)
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        adult_count = request.GET.get('adult_count')
        child_count = request.GET.get('child_count')

        return TemplateResponse(request, 'accommodation/create_reservation.html', {
            'accommodation': accommodation,
            'room': room,
            'MEDIA_URL': settings.MEDIA_URL,
            'images': accommodation_images,
            'check_in': check_in,
            'check_out': check_out,
            'adult_count': adult_count,
            'child_count': child_count,
            'cancellationpolicy': cancellationpolicy
        })

    def post(self, request, accommodation_pk, room_pk):
        data = request.data
        
        # user = request.user
        accommodation = Accommodation.objects.get(pk=accommodation_pk)
        room = Room.objects.get(pk=room_pk)
        
        check_in = data.get('check_in')
        check_out = data.get('check_out')
        guestcount = data.get('guestcount')

        
        serializer = ReservationSerializer(data=data)
        if serializer.is_valid():
            # now = timezone.now().date()
            check_in_date = serializer.validated_data.get('check_in')
            cancellation_policy_agreed = serializer.validated_data.get('cancellation_policy_agreed', False)
            terms_and_conditions_agreed = serializer.validated_data.get('terms_and_conditions_agreed', False)
           
            # 예약 생성 로직
            Reservation.objects.create(
                # user= user,
                accommodation=accommodation,
                room=room,
                check_in_date=check_in_date,
                check_out_date=serializer.validated_data.get('check_out'),
                check_in=check_in,
                check_out=check_out,
                guest_count=guestcount,
                reservation_amount=room.price,
                total_amount=room.price, 
                cancellation_policy_agreed=cancellation_policy_agreed,
                terms_and_conditions_agreed=terms_and_conditions_agreed
            )
            return JsonResponse({"success": "Reservation created successfully."}, status=status.HTTP_201_CREATED)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 지도 띄우기
def my_view(request, pk):
    accommodation = Accommodation.objects.get(pk=pk)

    # 리뷰와 좋아요 갯수 가져오기
    reviews = Review.objects.filter(accommodation=accommodation)
    images = AccommodationImage.objects.filter(accommodation=accommodation)  # Accommodation에 연결된 모든 이미지 가져오기

    reviews_count = reviews.count()
    likes_count = accommodation.like.count()

    # 리뷰의 평균 별점 계산
    if reviews_count > 0:
        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    else:
        average_rating = 0
    # 컨텍스트 딕셔너리에 GOOGLE_MAPS_API_KEY 추가
    context = {
        # 'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'accommodation': accommodation,
        'MEDIA_URL': settings.MEDIA_URL,
        'lat': accommodation.latitude,
        'lng': accommodation.longitude,
        'reviews': reviews,
        'reviews_count': reviews_count,
        'likes_count': likes_count,
        'average_rating': average_rating,
        'images': images if AccommodationImage.images else '',
        }
    # 컨텍스트와 함께 my_template.html 템플릿 렌더링
    return render(request, 'accommodation/accommodation_map.html', context)

    
# # 숙소 저장하기
# class SaveAccommodationView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def post(self, request, pk):
#         accommodation = get_object_or_404(Accommodation, pk=pk)
#         user = request.user
#         if user.is_anonymous:
#             return Response({"message": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)

#         else:
#             AccommodationLike.objects.create(user=user, accommodation=accommodation)
#             return Response({"message": "숙소가 저장되었습니다."}, status=status.HTTP_201_CREATED)

# # 숙소 저장 취소하기
# class UnsaveAccommodationView(APIView):
#     # permission_classes = [IsAuthenticated]
#     def post(self, request, pk):
#         accommodation = get_object_or_404(Accommodation, pk=pk)
#         user = request.user
#         if user.is_anonymous:
#             return Response({"message": "로그인이 필요합니다."}, status=status.HTTP_401_UNAUTHORIZED)
#         like = AccommodationLike.objects.filter(user=user, accommodation=accommodation).first()
#         if like:
#             like.delete()
#             return Response({"message": "숙소 저장이 취소되었습니다."}, status=status.HTTP_200_OK)
#         # else:
#         #     return Response({"message": "저장되지 않은 숙소입니다."}, status=status.HTTP_400_BAD_REQUEST)
  

class RoomDetailView(APIView):
    def get(self, request, accommodation_pk, room_pk):
        accommodation = Accommodation.objects.get(pk=accommodation_pk)
        room = Room.objects.get(pk=room_pk)
        room_images = RoomImage.objects.filter(room=room)
        
        context = {
            'MEDIA_URL': settings.MEDIA_URL,
            'accommodation': accommodation,
            'room': room,
            'room_images': room_images,
            'accommodation': accommodation,
            'name': room.name,
            'description': room.description,
            'capacity': room.capacity,
            'is_free_cancellation': room.is_free_cancellation,
            'includes_breakfast': room.includes_breakfast,
            'price': room.price,
            'check_in_time': room.check_in_time,
            'check_out_time': room.check_out_time,
            'guide': room.guide,
        }
        return render(request, 'accommodation/room_detail.html', context)
    



class ListReviews(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from .forms import ReviewForm
        
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from .models import Review
from .forms import ReviewForm

class CreateReview(View):
    def get(self, request, pk):
        accommodation = get_object_or_404(Accommodation, pk=pk)
        form = ReviewForm()
        return render(request, 'review/create_review.html', {'form': form, 'accommodation': accommodation})

    def post(self, request, pk):
        user = request.user
        accommodation = get_object_or_404(Accommodation, pk=pk)
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.accommodation = accommodation
            if request.user.is_authenticated:
                review.user = request.user
            else:
                anonymous_user, created = User.objects.get_or_create(username='anonymous_user')
                review.user = anonymous_user

            # review.user=user
            review.save()
            return redirect(reverse('review_detail', kwargs={'accommodation_pk': accommodation.pk, 'review_pk': review.pk}))
        else:
            return render(request, 'review/create_review.html', {'form': form, 'accommodation': accommodation})

class ReviewDetailView(APIView):
    def get(self, request, accommodation_pk, review_pk):
        accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
        accommodation_images = AccommodationImage.objects.filter(accommodation=accommodation) 

        review = get_object_or_404(Review, pk=review_pk)
        user = request.user
        context = {
            'accommodation': accommodation,
            'review': review,
            'MEDIA_URL': settings.MEDIA_URL,
            'images': accommodation_images,
        }
        return render(request, 'review/review_detail.html', context)


class ReviewUpdateView(View):
    def get(self, request, accommodation_pk, review_pk):
        accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
        review = get_object_or_404(Review, pk=review_pk, user=request.user)
        form = ReviewForm(instance=review)
        return render(request, 'review/update_review.html', {'form': form, 'accommodation': accommodation})

    def put(self, request, accommodation_pk, review_pk):
        accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
        review = get_object_or_404(Review, pk=review_pk, user=request.user)
        form = ReviewForm(request.PUT, instance=review)
        if form.is_valid():
            form.save()
            return redirect(reverse('review_detail', kwargs={'accommodation_pk': accommodation.pk, 'review_pk': review.pk}))
        return render(request, 'review/update_review.html', {'form': form, 'accommodation': accommodation})



from django.http import HttpResponseForbidden


class ReviewDeleteView(View):
    def delete(self, request, accommodation_pk, review_pk):
        accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
        review = get_object_or_404(Review, pk=review_pk, user=request.user)

        # 작성자가 현재 로그인한 사용자와 일치하는지 확인
        if review.user != request.user:
            return HttpResponseForbidden("You are not allowed to delete this review.")

        review.delete()
        return redirect(reverse('accommodation_detail', kwargs={'pk': accommodation.pk}))