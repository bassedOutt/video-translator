from google.cloud import texttospeech

def text_to_speech(text, output_audio_file, language_code="uk-UA", voice_name='uk-UA-Wavenet-A', audio_encoding=texttospeech.AudioEncoding.MP3):
    """Converts the given text to speech."""
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=audio_encoding
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open(output_audio_file, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file "{output_audio_file}"')

    pass

