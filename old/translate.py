# from google.cloud import translate_v2 as translate
#
# from old.generate_translated_audio import text_to_speech
#
#
# def translate_text(input_file_path, target_language="en"):
#     translate_client = translate.Client()
#
#     with open(input_file_path, "r") as file:
#         text = file.read()
#
#     result = translate_client.detect_language(text)
#     source_language = result["language"]
#
#     if source_language == target_language:
#         print("The source text is already in the target language.")
#         return text
#
#     translation = translate_client.translate(text, target_language=target_language)
#     translated_text = translation['translatedText']
#
#     return translated_text
#
# # input_file_path = "transcript.txt"
# # translated_text = translate_text(input_file_path, target_language="uk")
# #
# # text_to_speech(translated_text, "translated_audio.mp3")
