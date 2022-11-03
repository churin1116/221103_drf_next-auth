from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from testapp.views import *


router = routers.DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('note/', NoteView.as_view(), name='note'),
    path('note/<str:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('', include(router.urls)),
]