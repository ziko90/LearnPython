import io
from pprint import pprint

from google.cloud import speech


def run(audio_path, transcript_file_name):

    response = get_transcript(audio_path)
    write_to_file(transcript_file_name, response)


def write_to_file(transcript_file_name, response):
    with open(transcript_file_name, 'w') as f:
        for result in response.results:
            f.write((result.alternatives[0].transcript) + '\n')


def get_transcript(audio_path):
    client = speech.SpeechClient()

    with io.open(audio_path, 'rb') as audio_file:
        content = audio_file.read()
        audio = speech.types.cloud_speech_pb2.RecognitionAudio(content=content)

    config = speech.types.cloud_speech_pb2.RecognitionConfig(
        encoding = speech.enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz = 8000,
        language_code = 'en-US'
    )
    #detect
    return client.recognize(config, audio)


def fun():
    print("test")


if __name__ == "__main__":
    print("audio path")
    audio_path = input()
    print("txt file name")
    transcript_file_name = input()

    run(audio_path, transcript_file_name)
    fun()