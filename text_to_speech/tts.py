from gtts import gTTS
import os


text = "Hello Akshay, the is an example for voice synthesis using GTTS"
language = "en"
conv = gTTS(text = text, lang=language, slow = False)
conv.save("audio.mp3")
os.system("audio.mp3")

