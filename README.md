Speech to GPT


This project provides a simple conversational interface using OpenAI's GPT-3.5 language model. 
It allows users to interact with the AI through both text and speech. The core components of the project are:

1. `config.py`: This file contains configurations and settings for the project.
2. `texttospeech.py`: A module that converts text responses into speech using a text-to-speech engine.
3. `speechtotext.py`: A module that converts user speech input into text using a speech-to-text engine.
4. `gpt.py`: A module that utilizes OpenAI's GPT-3.5 language model to generate responses based on user inputs.

## Requirements

Before running this project, ensure you have the following installed:

- Python 3.6 or higher
- OpenAI Python SDK
- A valid OpenAI API key

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
```
1. Install Dependencies
```
pip install portaudio
pip install pyaudio
pip install openai
pip install playsound
pip install gtts
```
2. Open the keys.py file and add your key

```
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

Usage

To start a conversation with gpt, run the app

```
python app.py
```
