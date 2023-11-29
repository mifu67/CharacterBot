from openai import OpenAI
from apikey import GPT_KEY

client = OpenAI(api_key=GPT_KEY)
MODEL = 'gpt-3.5-turbo'
