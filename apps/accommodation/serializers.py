# serializers.py
from rest_framework import serializers
from .models import GuestInfo, TransportationInfo, Reservation, Room, Accommodation, Review

class GuestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestInfo
        fields = '__all__'

class TransportationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportationInfo
        fields = '__all__'

# class PaymentDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PaymentDetail
#         fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    guest_info = GuestInfoSerializer()
    transportation_info = TransportationInfoSerializer()
    # payment_detail = PaymentDetailSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        guest_info_data = validated_data.pop('guest_info')
        transportation_info_data = validated_data.pop('transportation_info')
        # payment_detail_data = validated_data.pop('payment_detail')

        guest_info = GuestInfo.objects.create(**guest_info_data)
        transportation_info = TransportationInfo.objects.create(**transportation_info_data)
        # payment_detail = PaymentDetail.objects.create(**payment_detail_data)

        reservation = Reservation.objects.create(
            guest_info=guest_info,
            transportation_info=transportation_info,
            reservation_amount=validated_data['reservation_amount'],
            total_amount=validated_data['total_amount'],
            check_in=validated_data['check_in'],  # 올바른 필드 이름 사용
            check_out=validated_data['check_out'],  # 올바른 필드 이름 사용
            guests=validated_data['guests'],
            # payment_detail=payment_detail,
            **validated_data
        )

        return reservation

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class AccommodationSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Accommodation
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'