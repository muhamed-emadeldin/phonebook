from django.urls import path, include
from .views import UserLogin, UserRegister, UserLogout
app_name = 'users'


urlpatterns = [
    path('', UserRegister.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogin.as_view(), name='logout'),
]