import pyttsx3
import wikipedia as wp

num = 4
text = wp.summary("Mac operating systems", sentences=num)
# text = "Git's design was inspired by BitKeeper"
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()