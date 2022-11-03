from rest_framework import generics, viewsets
from .serializers import NoteSerializer
from .models import Note
from rest_framework.permissions import AllowAny


class NoteView(generics.ListAPIView): # 一覧
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (AllowAny,)


class NoteDetailView(generics.RetrieveAPIView): # 詳細
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (AllowAny,)

class NoteViewSet(viewsets.ModelViewSet): # POST用
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (AllowAny,)