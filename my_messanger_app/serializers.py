from .models import *
from rest_framework import serializers


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Chat
        fields = ['name', 'owner']
        read_only_fields = ['id']


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    chats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Writer
        fields = ['id', 'username', 'avatar', 'chats']