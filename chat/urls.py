# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('writers/writers/', views.WritersList.as_view(), name='users_list'),
    path('writers/<int:pk>/', views.WriterDetail.as_view(), name='user_detail'),
    # path('room/<int:pk>/', views.room, name='room'),
    # path('create_room/', views.index, name='index'),
   # path('chats/', ChatList.as_view()),
   # path('chats/<int:pk>/', ChatDetail.as_view()),
    path('writers/<int:pk>/upgrade/', views.WriterUpgrade.as_view(), name='writer_edit'),
]
