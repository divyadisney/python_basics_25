from gtts import gTTS
import os
s=input("Enter a string: ")
content = gTTS(text=s,lang="en")
content.save("test_audio.mp3")
os.system("start test_audio.mp3")

