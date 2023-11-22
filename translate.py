import time
from deep_translator import MicrosoftTranslator
from deep_translator.exceptions import TooManyRequests


def translate_text(subtitles):
    translated_subtitles = []
    translator = MicrosoftTranslator(api_key='37bab7a0711e4a7a8e2e965381d0e123',region='francecentral',source='en', target='uk')

    for subtitle in subtitles:
        text = subtitle['text']
        start = subtitle['start']
        duration = subtitle['duration']

        # Translate and handle potential errors
        try:
            translated = translator.translate(text)
        except TooManyRequests:
            time.sleep(1)  # Wait for 1 second before retrying
            translated = translator.translate(text)

        translated_subtitle = {
            'text': translated,
            'start': start,
            'duration': duration
        }
        translated_subtitles.append(translated_subtitle)

        time.sleep(0.2)  # Wait 200 ms between each request to avoid hitting the rate limit

    print(translated_subtitles)
    return translated_subtitles
