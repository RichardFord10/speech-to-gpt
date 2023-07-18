from config import *
from gtts import gTTS
from playsound import playsound

class TextToSpeech:
    
    def __init__(self):
        pass

    def voicePlay(string):
        myobj = gTTS(text=string, lang='en', slow=False)
        # Check if the 'mp3' folder exists, and create it if it doesn't.
        if not os.path.exists("mp3"):
            os.makedirs("mp3")
            myobj.save("mp3/tts.mp3")
        else:
            myobj.save("mp3/tts.mp3")
            
        playsound('mp3/tts.mp3')
