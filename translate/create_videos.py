from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech5.mp3"

text = ""

response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=text
)

response.stream_to_file(speech_file_path)