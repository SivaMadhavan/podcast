from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user.serializers import CustomUserSerializer
from user.models import User

class CustomUserCreateView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        response = User().create(request)
        return Response(response, status=status.HTTP_201_CREATED)

