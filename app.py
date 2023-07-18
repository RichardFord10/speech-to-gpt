from config import *
from texttospeech import TextToSpeech
from speechtotext import SpeechToText
from gpt import ChatGpt        
    

string = SpeechToText.get_speech_text()
answer = ChatGpt.prompt(string)
TextToSpeech.voicePlay(answer)