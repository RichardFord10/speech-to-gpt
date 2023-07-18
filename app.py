from config import *
from texttospeech import TextToSpeech
from speechtotext import SpeechToText
from gpt import ChatGpt
import time

# Initialize ChatGpt instance
chatbot = ChatGpt()

# Store previous questions and answers as a list of tuples
previous_questions_and_answers = []

def listen_for_input():
    # Function to get user input and store it in a global variable
    global input_text
    input_text = SpeechToText.get_speech_text()

def converse():
    while True:
        # Listen for user input on a separate thread
        input_thread = threading.Thread(target=listen_for_input)
        input_thread.start()

        # Wait for user input with a timeout
        input_thread.join(timeout=LISTEN_TIMEOUT)

        # Check if the thread is still alive (input_thread is None after join with timeout)
        if input_thread.is_alive():
            # If the thread is still alive, it means we timed out waiting for input
            TextToSpeech.voicePlay("I didn't hear anything. Please try again.")
            continue

        # Check if the user wants to exit the conversation
        if input_text.lower() == 'exit conversation':
            TextToSpeech.voicePlay("Goodbye!")
            break

        # Generate a response using ChatGpt and respond to the user
        answer = chatbot.prompt(input_text, is_conversation=bool(previous_questions_and_answers), previous_questions_and_answers=previous_questions_and_answers)

        if answer.strip() != "":
            TextToSpeech.voicePlay(answer)
            # Add the current question and answer to the previous questions and answers list
            previous_questions_and_answers.append((input_text, answer))
        else:
            TextToSpeech.voicePlay("I'm sorry, I didn't get any response. Please try again.")

# Configuration - set the response timeout and listen timeout in seconds
RESPONSE_TIMEOUT = 5  # You can adjust this value as needed
LISTEN_TIMEOUT = 5    # Adjust this value based on the expected maximum pause between user responses

if __name__ == "__main__":
    converse()

