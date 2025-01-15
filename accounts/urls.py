from django.urls import path
from .views import CustomLoginView,UserRegistrationView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]