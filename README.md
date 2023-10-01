# Video Management API

The **Video Management API** is a Django application that allows you to create, append, and retrieve video files. You can use this API to create video records, append video chunks, and get the compiled video for a specific video ID.

## Endpoints

### Create Video (POST)

- Create a new video record.
- Method: POST
- Endpoint: `https://video-player-ct0v.onrender.com/create_video/`
- Response: JSON containing the created video ID.

Example Request:
```bash
curl -X POST https://video-player-ct0v.onrender.com/create_video/
```

Example Response:
```json
{
    "video_id": 14
}
```

### Append Video Chunk (POST)

- Append a video chunk to an existing video.
- Method: POST
- Endpoint: `https://video-player-ct0v.onrender.com/append_video/<video_id>/`
- Request Body: Video chunk data in binary format.
- Response: JSON with a success message.

For the first chunk:
```json
{
    "message": "Video added successfully"
}
```

For subsequent chunks:
```json
{
    "message": "Video appended and joined successfully"
}
```

### Get Video (GET)

- Retrieve the compiled video for a specific video ID.
- Method: GET
- Endpoint: `https://video-player-ct0v.onrender.com/get_video/<video_id>/`
- Response: Video file.

Example Request:
```bash
curl https://video-player-ct0v.onrender.com/get_video/14/
```

## Usage

1. Create a new video record using the "Create Video" endpoint. Note the returned `video_id`.

2. Append video chunks to the video using the "Append Video Chunk" endpoint. Ensure you include the `video_id` in the URL.

3. Once all video chunks are appended, you can retrieve the compiled video using the "Get Video" endpoint with the `video_id`.

## Deployment

The API has been deployed and can be accessed at the following base URL:
- Base URL: `https://video-player-ct0v.onrender.com/`

## Known Limitations and Assumptions

- This API does not implement authentication or authorization.
- Video files are appended sequentially, so ensure you send the chunks in the correct order.
- It takes time to append video chunks