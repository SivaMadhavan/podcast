from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer, LogoutSerializer, VerificationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.views import APIView
from .utils import Utils
from django.contrib.auth import get_user_model
from .strings import USER_REG_EMAIL_SUBJECT, USER_REG_EMAIL_BODY
from django.conf import settings

User = get_user_model()


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        try:
            action = request.get("action")
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            relative_link = reverse('email-verify')
            abs_url = settings.BASE_URL + relative_link + "?code=" + str(user.verification_code)
            data = {'email_body': USER_REG_EMAIL_BODY.format(user.username,abs_url), 'to_email': user.email,'email_subject': USER_REG_EMAIL_SUBJECT}
            Utils.send_email(data)
            return Response({"email": user.email, "username": user.username}, status=status.HTTP_201_CREATED)
        except Exception as e:
            import traceback
            print(traceback.print_exc())


class VerificationView(APIView):
    serializer_class = VerificationSerializer

    def post(self, request):
        try:
            data = request.data
            data["code"] = request.GET.get("code")
            serializer = self.serializer_class(data=data)
            if not serializer.is_valid():
                return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            user = serializer.validated_data
            user.set_password(data.get("password"))
            user.save()
            return Response({"message":"Your password has been successfully set"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
