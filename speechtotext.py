import speech_recognition as sr
from texttospeech import TextToSpeech


r = sr.Recognizer()

# Reading Microphone as source
class SpeechToText:
    
    def __init__(self):
        pass

    def get_speech_text(max_attempts=3, listen_timeout=5):
        for _ in range(max_attempts):
            with sr.Microphone() as source:
                print("Talk")
                audio_text = r.listen(source, timeout=listen_timeout)
                print("Input Received, moving on...")
            try:
                # Attempt to recognize speech from the audio_text
                recognized_text = r.recognize_google(audio_text)
                if recognized_text:
                    return recognized_text
                else:
                    TextToSpeech.voicePlay("Sorry, I did not get that. Let's try again.")
            except sr.UnknownValueError:
                TextToSpeech.voicePlay("Sorry, I could not understand what you said. Let's try again.")
            except sr.RequestError:
                TextToSpeech.voicePlay("Sorry, there was an issue connecting to the speech recognition service. Let's try again.")

        return "Sorry, we couldn't understand your input after multiple attempts."