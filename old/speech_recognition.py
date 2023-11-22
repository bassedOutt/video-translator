from google.cloud import speech
from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US',
        enable_word_time_offsets=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    transcript_file_path = "../transcript.txt"
    captions_file_path = "../captions.txt"
    write_transcription_and_captions(response, transcript_file_path, captions_file_path)

def write_transcription_and_captions(response, transcript_file_path, captions_file_path):
    with open(transcript_file_path, "w") as transcript_file, open(captions_file_path, "w") as captions_file:
        for result in response.results:
            for alternative in result.alternatives:
                # Write the full transcript to one file
                transcript_file.write("{}\n".format(alternative.transcript))

                # Write the captions with timestamps to another file
                for word_info in alternative.words:
                    word = word_info.word
                    start_time = word_info.start_time.total_seconds()
                    end_time = word_info.end_time.total_seconds()
                    captions_file.write(f"{word} ({start_time} - {end_time})\n")

bucket_name = "raw-audios"
source_file_name = "../audio_compressed.wav"
destination_blob_name = "uploaded_audio.wav"
upload_blob(bucket_name, source_file_name, destination_blob_name)
gcs_uri = f"gs://{bucket_name}/{destination_blob_name}"
transcribe_gcs(gcs_uri)

