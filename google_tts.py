import os
from gtts import gTTS
from pydub import AudioSegment

def synthesize_speech(text, filename):
    tts = gTTS(text=text, lang='uk')
    tts.save(filename)
    return AudioSegment.from_mp3(filename)

def create_translated_audio_file(captions):
    audio_clips = []
    for i, caption in enumerate(captions):
        filename = f"temp_{i}.mp3"
        audio_clip = synthesize_speech(text=caption['text'], filename=filename)
        audio_clips.append((audio_clip, caption['start'], caption['duration']))

        # Clean up temporary file
        os.remove(filename)

    combined_audio = AudioSegment.silent(duration=0)
    current_time = 0.0

    for clip, start, duration in audio_clips:
        # Add silence until the start of this clip
        silence_duration = int((start - current_time) * 1000)  # Convert to milliseconds
        combined_audio += AudioSegment.silent(duration=silence_duration)

        # Add the audio clip
        clip_duration = int(duration * 1000)
        combined_audio += clip[:clip_duration]

        current_time = start + duration

    # Export the combined audio
    audio_file_name = "final_audio.mp3"
    combined_audio.export(audio_file_name, format="mp3")
    return audio_file_name
