from config import openai, keys

openai.api_key = keys.openai_key

TEMPERATURE = 0.5
MAX_TOKENS = 500
FREQUENCY_PENALTY = 0
PRESENCE_PENALTY = 0.6
MAX_CONTEXT_QUESTIONS = 10
ENGINE = "text-davinci-002"

class ChatGpt: 

    def __init__(self):
        pass

    def prompt(self, prompt, new_question=None, is_conversation=False, previous_questions_and_answers=None):
        if not is_conversation or previous_questions_and_answers is None:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                top_p=1.0,
                frequency_penalty=FREQUENCY_PENALTY,
                presence_penalty=PRESENCE_PENALTY
            )
            return response['choices'][0]['text']
        else:
            messages = [
                {"role": "system", "content": prompt},
            ]
            # add the previous questions and answers
            for question, answer in previous_questions_and_answers[-MAX_CONTEXT_QUESTIONS:]:
                messages.append({"role": "user", "content": question})
                messages.append({"role": "assistant", "content": answer})
            
            # Add the new question if provided, or set it to an empty string
            new_question = new_question or ""
            messages.append({"role": "user", "content": new_question})

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS,
                top_p=1.0,
                frequency_penalty=FREQUENCY_PENALTY,
                presence_penalty=PRESENCE_PENALTY
            )
            return completion['choices'][0]['message']['content']