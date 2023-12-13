from youtube_transcript_api import YouTubeTranscriptApi
import re
from download import download_video
from new_audio import create_translated_audio_file
from replace_audio import replace_audio_in_video
from translate import translate_text


def extract_video_id(url):
    regex = r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.search(regex, url)

    if match:
        return match.group(1)
    else:
        return "Invalid YouTube URL"


if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    file_name = download_video(video_url)
    video_id = extract_video_id(video_url)
    srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
    translated_captions = translate_text(srt)
    audio_file_name = create_translated_audio_file(translated_captions)
    replace_audio_in_video(file_name, audio_file_name, 'final'+file_name)
