from django.urls import path
from .views import RegisterView, SingInView, activate
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('sign_up/', RegisterView.as_view(), name='sing_up'),
    path('login/', SingInView.as_view(), name='login'),
    path('activate/<str:activation_code>/', activate, name='activate'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
