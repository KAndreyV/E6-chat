from django.urls import path
from .views import (WritersList, WriterDetail, WriterUpgrade, ChatList, ChatDetail,
                    )


urlpatterns = [
   path('', WritersList.as_view(), name='users_list'),
   path('<int:pk>/', WriterDetail.as_view(), name='user_detail'),
   path('chats/', ChatList.as_view()),
   path('chats/<int:pk>/', ChatDetail.as_view()),
   path('<int:pk>/upgrade/', WriterUpgrade.as_view(), name='writer_edit'),
]