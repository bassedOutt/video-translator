from moviepy.editor import VideoFileClip, AudioFileClip

def replace_audio_in_video(video_file, new_audio_file, output_video_file):
    """Replaces the audio track in the video file with new audio."""
    video = VideoFileClip(video_file)
    new_audio = AudioFileClip(new_audio_file)

    # Setting the audio of the video to the new audio
    video_with_new_audio = video.set_audio(new_audio)

    # Writing the result to a file
    video_with_new_audio.write_videofile(output_video_file, codec='libx264', audio_codec='aac')