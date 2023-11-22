from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)
    print(f"Audio extracted and saved to {output_audio_path}")

if __name__ == "__main__":
    # video_path = input("Enter the path of the video file: ")
    # output_audio_path = input("Enter the path to save the extracted audio (e.g., output_audio.wav): ")
    video_path = '../Can you present a product.mp4'
    output_audio_path = 'audio.wav'
    extract_audio_from_video(video_path, output_audio_path)
