from gtts import gTTS
import wikipedia

tt = wikipedia.summary("Zorin OS")
tts = gTTS(tt)

tts.save('hello.mp3')