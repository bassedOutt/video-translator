

import os

from pydub import AudioSegment

from azure_texttospeech import synthesize_speech_azure_to_file


def create_translated_audio_file(captions):
    audio_clips = []
    for i, caption in enumerate(captions):
        filename = f"temp_{i}"
        audio_clip = synthesize_speech_azure_to_file(text=caption['text'], filename=filename)
        if audio_clip is not None:
            audio_clips.append((audio_clip, caption['start'], caption['duration']))
        else:
            print(f"Skipping caption {i} due to synthesis error.")

        if os.path.exists(filename):
            os.remove(filename)

    combined_audio = AudioSegment.silent(duration=0)
    current_time = 0.0

    for clip, start, duration in audio_clips:
        silence_duration = int((start - current_time) * 1000)
        combined_audio += AudioSegment.silent(duration=silence_duration)

        clip_duration = int(duration * 1000)
        combined_audio += clip[:clip_duration]

        current_time = start + duration

    audio_file_name = "final_audio.mp3"
    combined_audio.export(audio_file_name, format="mp3")
    return audio_file_name
