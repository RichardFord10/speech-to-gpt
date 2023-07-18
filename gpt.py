from config import openai, keys

openai.api_key = keys.openai_key

class ChatGpt: 

  def __init__(self):
    pass

  def prompt(prompt):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0,
    max_tokens=186,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0)
    return response['choices'][0]['text']
