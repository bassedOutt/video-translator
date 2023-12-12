import os
import tempfile

import azure.cognitiveservices.speech as speechsdk
from pydub import AudioSegment


def synthesize_speech_azure_to_file(text, filename, voice_name='uk-UA-PolinaNeural', fileformat='mp3'):
    speech_config = speechsdk.SpeechConfig(subscription="abbf758f6dbb456fadc69b127e55edec", region="francecentral")
    speech_config.speech_synthesis_voice_name = voice_name

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    audio_config = speechsdk.audio.AudioOutputConfig(filename=temp_file.name)
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        print(f"Speech synthesis canceled: {result.cancellation_details.reason}")
        if result.cancellation_details.reason == speechsdk.CancellationReason.Error:
            if result.cancellation_details.error_details:
                print(f"Error details: {result.cancellation_details.error_details}")
        return None

    temp_file.close()
    audio_segment = AudioSegment.from_wav(temp_file.name)

    os.remove(temp_file.name)

    fullfilename = filename + ".mp3"
    audio_segment.export(fullfilename, format=fileformat)
    print(f"Audio saved to {filename}")

    return audio_segment

