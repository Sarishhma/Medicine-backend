from django.urls import path
# from api.views.login import RegisterUserAPIView, LoginUserAPIView,ForgotPasswordAPIView, ResetPasswordAPIView, CustomTokenObtainPairView
from api.views.Register import RegisterUserView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name="register-user")

]