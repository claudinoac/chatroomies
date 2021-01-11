from django.urls import path
from django.contrib.auth.views import LoginView
from apps.login.views import SignUpView

app_name = "chatroom"
urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup")
]
