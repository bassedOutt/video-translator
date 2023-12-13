from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        video_stream.download("")
        print(f"Video downloaded successfully: {video_stream.default_filename}")
        return video_stream.default_filename
    except Exception as e:
        print(f"An error occurred: {e}")
