from gtts import gTTS
tts = gTTS('hello', lang='en')
tts.save('hello.mp3')
print(">>file created")