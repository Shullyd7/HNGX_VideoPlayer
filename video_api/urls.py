from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.upload_video, name='upload_video'),
    path('play/<int:video_id>/', views.play_video, name='play_video'),
]
