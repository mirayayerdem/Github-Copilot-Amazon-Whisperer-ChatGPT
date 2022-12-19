import openai
from decouple import config

openai.api_key = config('OPENAI_API_KEY')

def return_response(given_prompt):
    given_prompt += "Time Complexity:"

    response = openai.Completion.create(
        engine="code-davinci-001",
        prompt= given_prompt,
        temperature=0,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text