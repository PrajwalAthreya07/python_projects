#install and import "gtts" & "playsound" packages
from gtts import gTTS
from playsound import playsound

#set audio to mp3 and laguage as per preference
audio = 'speech.mp3'
language = 'en'

#inside the text include whatever that has to be recited
sp = gTTS(text="Hi how are you?",
          lang = language,slow=True)

#save the audio and play the sound
sp.save(audio)
playsound(audio)
