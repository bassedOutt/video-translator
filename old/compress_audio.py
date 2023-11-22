import ffmpeg

def compress_audio(video_path, output_audio_path, audio_bitrate="32k"):
    try:
        (
            ffmpeg
            .input(video_path)
            .output(output_audio_path, audio_bitrate=audio_bitrate, ac=1, ar="16000")
            .run(overwrite_output=True)
        )
        print(f"Compressed audio extracted and saved to {output_audio_path}")
    except ffmpeg.Error as e:
        print("Error:", e)

# Example usage:
compress_audio("../Can you present a product.mp4", "audio_compressed.wav")
