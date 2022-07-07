from rest_framework.response import Response
from rest_framework.views import APIView

from main.api.guest_data.serializers import GuestDataSerializer


class GuestDataAPIView(APIView):
    def post(self, request):
        guest_data = {
            'name': request.data['guests'][0]['first_name'],
            'room': request.data['room'],
            'checkin_date': request.data['checkin_date'],
            'checkout_date': request.data['checkout_date']
        }

        serializer = GuestDataSerializer(data=guest_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


