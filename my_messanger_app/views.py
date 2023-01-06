from django.views.generic import (ListView, DetailView, UpdateView, DeleteView, )
from .models import Writer, User, Chat
from rest_framework import viewsets, generics
from .serializers import *
from django.http import HttpResponse
import json
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404


class WritersList(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'
    paginate_by = 10


class WriterDetail(DetailView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'


class WriterUpgrade(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('my_messanger_app.change_writer',)
    form_class = WriterForm
    model = Writer
    template_name = 'writer_edit.html'
    context_object_name = 'writer'


class ChatViewSet(viewsets.ModelViewSet):
   queryset = Chat.objects.all()
   serializer_class = ChatSerializer


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


def get_chat(_, pk):
    chat = Chat.objects.get(pk=pk)
    return HttpResponse(content=chat, status=200)


def get_chats(_):
    chats = Chat.objects.all()
    return HttpResponse(content=chats, status=200)


# def create_chat(LoginRequiredMixin, request, serializer):
#     body = json.loads(request.body.decode('utf-8'))
#     chat = Chat.objects.create(
#         name=body['name'],
#     )
#     return serializer.save(author=request.user)


def edit_chat(request, pk):
    body = json.loads(request.body.decode('utf-8'))
    chat = Chat.objects.get(pk=pk)
    for attr, value in body.items():
        setattr(chat, attr, value)
    chat.save()
    return HttpResponse(content=chat, status=200)


def delete_chat(_, pk):
    chat = Chat.objects.get(pk=pk).delete()
    return HttpResponse(status=204)


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})
