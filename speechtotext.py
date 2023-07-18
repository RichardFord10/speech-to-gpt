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
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                return r.recognize_google(audio_text)
            except:
                print("Sorry, I did not get that")