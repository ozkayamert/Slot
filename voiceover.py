from gtts import gTTS

metin = input("Enter the text to be spoken: ")

tts = gTTS(text=metin,lang="en")
tts.save("ses.mp3")