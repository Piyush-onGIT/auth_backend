from django.urls import path
from account.views import UserRegistrationViews, UserLoginView, UserProfileView, UserChangePasswordView, SendPasswordResetEmailView

urlpatterns = [
    path('register/', UserRegistrationViews.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
]