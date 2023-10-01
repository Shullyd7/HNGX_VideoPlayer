from django.urls import path
from . import views

urlpatterns = [
    path('create_video/', views.create_video, name='create_video'),
    path('append_video/<int:video_id>/', views.append_video, name='append_video'),
    path('get_video/<int:video_id>/', views.get_video, name='get_video'),
]