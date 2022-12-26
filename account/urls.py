from django.urls import path
from account.views import UserRegistrationViews, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]