from django.urls import path, include
from account.views import UserRegistrationViews

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
]