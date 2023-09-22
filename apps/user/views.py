from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from apps.user.forms import SignUpForm, SignInForm
from apps.user.models import User


class UserListView(LoginRequiredMixin, ListView):
    """Class based views are the best for others"""

    model = User
    template_name = "user/user-list.html"
    context_object_name = "user_list"


class UserAccountView(LoginRequiredMixin, TemplateView):
    template_name = "user/user-account.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user/sign-up.html"
    success_url = reverse_lazy("user-account")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class SignInView(LoginView):
    login = "sign-in"
    template_name = "user/sign-in.html"
    authentication_form = SignInForm


class UserLogoutView(LogoutView):
    logout = "logout"
