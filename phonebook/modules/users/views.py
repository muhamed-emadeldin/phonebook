from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import UserLogin, UserRegister

class UserRegister(CreateView):
    template_name           = 'users/sign-up.html'
    form_class              = UserRegister
    success_url             = reverse_lazy('users:login')

class UserLogin(LoginView):
    template_name           = "users/sign-in.html"
    authentication_form     = UserLogin
    success_url             = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class UserLogout(LogoutView):
    next_page   = ''