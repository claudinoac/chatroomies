from apps.chatroom.views import hello_view
from django.urls import path

urlpatterns = [
    path('', hello_view)
]
