from apps.chatroom.views import ChatroomView, chatroom_add_view
from django.urls import path

app_name = "chatroom"
urlpatterns = [
    path('<int:chatroom_id>/', ChatroomView.as_view(), name="chatroom_view"),
    path('add/', chatroom_add_view)
]
