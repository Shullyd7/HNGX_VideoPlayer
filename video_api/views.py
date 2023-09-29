from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.shortcuts import render
# Create your views here.


@api_view(['POST'])
def upload_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def play_video(request, video_id):
    try:
        video = Video.objects.get(pk=video_id)
        return render(request, 'video_player.html', {'video': video})
    except Video.DoesNotExist:
        return HttpResponseNotFound("Video not found")
        return Response({'error': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
