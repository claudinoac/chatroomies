from apps.chatroom.views import ChatroomView, chatroom_add_view
from django.urls import path

urlpatterns = [
    path('<int:chatroom_id>/', ChatroomView.as_view()),
    path('add/', chatroom_add_view)
]
