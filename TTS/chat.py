import asyncio

from dotenv import load_dotenv
import speech_recognition as sr
from openai import OpenAI
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer
load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=speech,
        instructions="Always speak in cheerful manner with delight and happiness",
        response_format="pcm",
    ) as response :
        await LocalAudioPlayer().play(response)
SYSTEM_PROMPT = """
You're an expert voice agent. You are given the transcript of what
the user has said using voice.

You need to output as if you are a voice agent and whatever you speak
will be converted back to audio using AI and played back to user.
"""

def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=2)
        r.pause_threshold = 3
        r.phrase_threshold = 0.3
        r.non_speaking_duration = 1

        while True:
            try:
                print("\nSpeak Something...")
                audio = r.listen(source, timeout=5, phrase_time_limit=10)

                print("Processing Audio... (STT)")
                stt = r.recognize_google(audio)
                print("You Said:", stt)

                # ✅ CORRECT - AI response is in the try block, after STT succeeds
                print("Getting AI Response...")
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": stt}
                    ]
                )
                print("AI Response:", response.choices[0].message.content)
                asyncio.run(tts(speech=response.choices[0].message.content))

            except sr.UnknownValueError:
                print("❌ Couldn't understand. Please speak clearly and try again.")
            except sr.WaitTimeoutError:
                print("⏱️ No speech detected. Listening again...")
            except sr.RequestError as e:
                print(f"🌐 Google API error: {e}")

if __name__ == "__main__":
    main()
