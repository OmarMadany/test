from gtts import gTTS
import os

text = input("Enter text to convert to speech: ")
tts = gTTS(text)
tts.save("speech.mp3")
os.system("start speech.mp3")
