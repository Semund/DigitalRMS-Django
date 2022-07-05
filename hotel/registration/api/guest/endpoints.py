import datetime

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.api.guest.serializers import GuestDataSerializer
from registration.models import Booking


class GuestAPIView(APIView):
    def post(self, request):
        room_number = request.data['room_number']
        passport_data = request.data['passport_data']

        bookings_by_room = get_object_or_404(Booking,
                                             room__number=room_number,
                                             guests__passport_number__endswith=passport_data,
                                             checkin_date__lte=datetime.date.today(),
                                             checkout_date__gte=datetime.date.today(),
                                             )

        return Response(GuestDataSerializer(bookings_by_room).data)
