from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Note
        fields = ('id', 'user', 'index', 'phase', 'note', 'created_at')