from django.urls import path
from apps.user import views

urlpatterns = [
    path("", views.UserListView.as_view(), name='user-list'),
    path('account/sign-up', views.SignUpView.as_view(), name="sign-up"),
    path('account/sign-in', views.SignInView.as_view(), name="sign-in"),
    path('account', views.UserAccountView.as_view(), name="user-account"),
    path('account/logout', views.UserLogoutView.as_view(), name="logout"),
]
