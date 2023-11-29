from openai import OpenAI
from apikey import GPT_KEY, TOG_KEY
from multiprocessing import Pool
import together

client = OpenAI(api_key=GPT_KEY)
MODEL = 'gpt-3.5-turbo'

together.api_key = TOG_KEY

YOUNG = 'mifu67@stanford.edu/llama-2-7b-chat-young-han-new-data-6--1e-05-2023-11-22-21-56-35'
MIDDLE = ''
OLD = ''

def generate_interview():
    pass

def evaluate_memorization():
    pass

def evaluate_personality():
    pass

def evaluate_values():
    pass

def evaluate_hallu():
    pass

def evaluate_stability():
    pass

def main():
    pass



