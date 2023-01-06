from django import forms
from .models import Chat, Writer


# class ChatForm(forms.ModelForm):
#     class Meta:
#         model = Chat
#         fields = ['name']
#         exclude = ['writer']


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['first_name', 'last_name', 'email', 'avatar']
        exclude = ['user_id']
