from tqdm import tqdm
import logging
from google.cloud import texttospeech_v1 as texttospeech
from google.oauth2 import service_account
import os
from cache import Md5Cache, Cache
import ffmpeg


class GoogleVoicer:
    def __init__(self, core_key: str, base_path: str=""):
        self.cache = Md5Cache("output/cache/")
        self.slow_cache = Cache(f"output/74/{base_path}{core_key}")
        credentials = service_account.Credentials.from_service_account_file(
            'keys/autodub-391820-eaa04bea1213.json')
        self.client = texttospeech.TextToSpeechClient(credentials=credentials)

        # Specify the language and voice
        self.voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-F",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )
        # Specify the audio configuration
        self.audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1.0,)

    def speak(self, name, caption):
        # escape to file system outputable name
        name = name.replace("/", "_")
        name = name.replace(":", "_")
        name = name.replace(" ", "_")
        name = name.replace("'", "_")
        name = name.replace("?", "_")
        cached = self.slow_cache.get(name, "mp3")
        if cached:
            return cached

        caption = f"<speak>{caption}</speak>"
        # tqdm.write(f"Speaking: {caption}")
        synthesis_input = texttospeech.SynthesisInput(ssml=caption)
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=self.voice,
            audio_config=self.audio_config)
        file = self.cache.get_key_path(caption, "mp3")
        with open(file, 'wb') as out:
            out.write(response.audio_content)

        return ffmpeg.slowdown(name, file, self.slow_cache)
