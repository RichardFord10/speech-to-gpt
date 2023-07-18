import speech_recognition as sr

r = sr.Recognizer()

# Reading Microphone as source
class SpeechToText:
    
    def __init__(self):
        pass

    def get_speech_text():
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Input Received, moving on...")
        try:
            # Attempt to recognize speech from the audio_text
            recognized_text = r.recognize_google(audio_text)
            if recognized_text:
                return recognized_text
            else:
                return "Sorry, I did not get that"
        except sr.UnknownValueError:
            return "Sorry, I could not understand what you said"
        except sr.RequestError:
            return "Sorry, there was an issue connecting to the speech recognition service"