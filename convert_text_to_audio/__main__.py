from pathlib import Path
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('CHATGPT_KEY'))

text_files = os.listdir(f"{Path(__file__).parent}/text_files")

for text_file in text_files:
    f = open(f"{Path(__file__).parent}/text_files/{text_file}", "r")
    text_content = f.read()

    response = client.audio.speech.create(
        model="tts-1-hd",
        voice="alloy",
        input=text_content,
    )
    
    audio_file_name = f"{text_file.split('.')[0]}.mp3"

    response.write_to_file(f"{Path(__file__).parent}/audio_files/{audio_file_name}")
    
    f.close()

