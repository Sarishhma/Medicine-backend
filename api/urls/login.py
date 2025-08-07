from django.urls import path
from api.views.login import LoginUserView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login-user'),
]
