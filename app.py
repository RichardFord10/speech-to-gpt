from config import *
from texttospeech import TextToSpeech
from speechtotext import SpeechToText
from gpt import ChatGpt

# Initialize ChatGpt instance
chatbot = ChatGpt()

def converse():
    while True:
        # Listen for user input
        input_text = SpeechToText.get_speech_text()

        # Check if the user wants to exit the conversation
        if input_text.lower() == 'exit conversation':
            TextToSpeech.voicePlay("Goodbye!")
            break

        # Generate a response using ChatGpt and respond to the user
        answer = chatbot.prompt(input_text)
        TextToSpeech.voicePlay(answer)

if __name__ == "__main__":
    converse()
