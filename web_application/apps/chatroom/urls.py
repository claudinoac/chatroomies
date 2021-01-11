from django.urls import path

from apps.chatroom.views import ChatroomView, ChatroomListView, ChatroomAddView

app_name = "chatroom"
urlpatterns = [
    path("<int:chatroom_id>/", ChatroomView.as_view(), name="chatroom_view"),
    path("", ChatroomListView.as_view(), name="chatroom_list"),
    path("add", ChatroomAddView.as_view(), name="chatroom_add")
]
