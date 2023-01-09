from django.urls import path
from . import views


urlpatterns = [
   path('', views.WritersList.as_view(), name='users_list'),
   path('<int:pk>/', views.WriterDetail.as_view(), name='user_detail'),
   path('room/<int:pk>/', views.room, name='room'),
   path('create_room/', views.index, name='index'),
   # path('chats/', ChatList.as_view()),
   # path('chats/<int:pk>/', ChatDetail.as_view()),
   path('<int:pk>/upgrade/', views.WriterUpgrade.as_view(), name='writer_edit'),
]