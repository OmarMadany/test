from gtts import gTTS
import os

text = input("Enter text to convert to speech: ")
tts = gTTS(text)
tts.save("speech.mp3")
print(f"\nSpeech file created successfully: speech.mp3")
print("You can download and play the MP3 file from the file browser.")
