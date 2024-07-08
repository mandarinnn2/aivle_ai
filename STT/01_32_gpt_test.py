import openai
import pandas as pd

client = openai.OpenAI(api_key = 'gpt key 작성해주세요')

with open("text_format.txt", "r", encoding='UTF8') as f:
    example = f.read()

print(example)


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)