import whisper
from celery import shared_task

from video_api.models import Video


@shared_task
def transcribe_video(video_id, audio_path):
    try:
        video = Video.objects.get(pk=video_id)
    except Video.DoesNotExist:
        return

    if not video.upload:
        return

    # Use Whisper to transcribe the audio
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)

    # Save the transcription result in the Video model
    video.transcription = result["text"]
    video.save()

