from rest_framework import serializers

from core.models import Todo
from user.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    """Serializer for Todo objects"""

    user = UserSerializer(read_only=True)

    class Meta:
        model = Todo
        fields = ('id', 'user', 'title', 'content', 'created_at', 'is_completed')
        read_only_fields = ('id', 'user',)