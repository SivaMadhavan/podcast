from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class UserAuthentication(TokenAuthentication):

    def authenticate(self, request):
        response = super().authenticate(request)
        # if not response:
        #     AuthenticationFailed("Authentication Failed")
        # else:
        #     if isinstance(response, tuple):
        #         request.user, token = response
        return super().authenticate(request)
