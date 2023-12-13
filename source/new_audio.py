

import os

from pydub import AudioSegment

from azure_texttospeech import synthesize_speech_azure_to_file


def create_translated_audio_file(captions):
    audio_clips = []
    for i, caption in enumerate(captions):
        filename = f"temp_{i}"
        mp3_filename = synthesize_speech_azure_to_file(text=caption['text'], filename=filename)
        if mp3_filename:
            audio_clip = AudioSegment.from_mp3(mp3_filename)
            audio_clips.append((audio_clip, caption['start'], caption['duration']))

            # Delete the MP3 file after processing
            if os.path.exists(mp3_filename):
                os.remove(mp3_filename)
        else:
            print(f"Skipping caption {i} due to synthesis error.")

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

if __name__ == "__main__":
    captions = [{'text': 'Що таке Бог?', 'start': 0.26, 'duration': 1.579}, {'text': 'Що значить думати про щось священне і величніше за нас, нескінченне і безмежне?', 'start': 4.14, 'duration': 6.32}]
    create_translated_audio_file(captions)
