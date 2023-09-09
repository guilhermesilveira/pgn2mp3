from tqdm import tqdm
import logging
from google.cloud import texttospeech_v1 as texttospeech
from google.oauth2 import service_account
import os
from cache import Cache


class GoogleVoicer:
    def __init__(self, core_key: str):
        self.cache = Cache(f"output/raw/{core_key}")
        self.slow_cache = Cache(f"output/74/{core_key}")
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
        name = name.replace("?", "_")
        cached = self.slow_cache.get(name, "mp3")
        if cached:
            return cached

        caption = f"<speak>{caption}</speak>"
        tqdm.write(f"Speaking: {caption}")
        synthesis_input = texttospeech.SynthesisInput(ssml=caption)
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=self.voice,
            audio_config=self.audio_config)
        file = self.cache.get_key_path(name, "mp3")
        with open(file, 'wb') as out:
            out.write(response.audio_content)

        # ffmpeg file to slow down to 74% with same file name but folder same_folder/74/
        # ffmpeg -i file -filter:a "atempo=0.74" -vn new_file
        # create the string
        new_name = self.slow_cache.get_key_path(name, 'mp3')
        ffmpeg_string = f"ffmpeg -y -i '{file}' -filter:a \"atempo=0.74\" -vn '{new_name}'"
        # runs it, if fails, stop
        if os.system(ffmpeg_string):
            logging.error(f"Failed to run ffmpeg command: {ffmpeg_string}")
            exit(1)
        return new_name
