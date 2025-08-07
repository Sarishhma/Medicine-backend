from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from app.models import SimpleUser
from api.serializers.login import LoginSerializer

class LoginUserView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = SimpleUser.objects.get(username=username)
            except SimpleUser.DoesNotExist:
                return Response({'error': 'Invalid username'}, status=status.HTTP_401_UNAUTHORIZED)

            if check_password(password, user.password):

                return Response({'username': user.username , "user_id": user.id})
            else:
                return Response({'error': 'Invalid  password'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
