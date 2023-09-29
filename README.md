# Video Upload and Playback API

The **Video Upload and Playback API** is a Django-based web application that allows users to upload video files and play them back through a web interface.

## Usage

### Upload Video

To upload a video, make a POST request to the following endpoint:

- Endpoint: `https://shully.pythonanywhere.com/api/upload/`
- Method: POST
- Request Body: Form data with the video file using the name 'upload'.

Example using `curl`:

```bash
curl -X POST -F "upload=@/path/to/your/video.mp4" https://shully.pythonanywhere.com/api/upload/
```

Response:

```json
{
    "id": 3,
    "upload": "/media/videos/file_example_MP4_480_1_5MG.mp4"
}
```

### Play Video

To play a previously uploaded video, visit the following URL in a web browser:

- URL: `https://shully.pythonanywhere.com/play/<int:video_id>/`

Replace `<int:video_id>` with the actual video ID returned when you uploaded the video. This will render a video player, allowing you to play the video.

## Installation

To set up this project locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Shullyd7/HNGX_VideoPlayer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd HNGX_VideoPlayer
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Access the API at `http://127.0.0.1:8000/api/upload/` for uploading videos and use the `/play/<int:video_id>/` endpoint for video playback.

## Hosting

The application is hosted on PythonAnywhere at `https://shully.pythonanywhere.com/`.

## Requirements

- Django==4.2.5
- djangorestframework==3.14.0