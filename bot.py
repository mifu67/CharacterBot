"""
Main file for CharacterBot
"""
import os
import together
from dotenv import load_dotenv

load_dotenv()

together.api_key = os.getenv('TOGETHER_API_KEY')

MODEL_SET = set(['YOUNG', 'REGULAR', 'OLD'])
MODELS = {
    "YOUNG" : "mifu67@stanford.edu/llama-2-7b-chat-young-han-new-data-6--1e-05-2023-11-22-21-56-35",
    "REGULAR" : "mifu67@stanford.edu/llama-2-7b-chat-middle-han-10--1e-05-2023-11-29-03-08-42",
    "OLD" : "mifu67@stanford.edu/llama-2-7b-chat-old-han-third-20--1e-05-2023-11-27-03-46-19",

}
SYSTEM_PROMPT = 'I want you to act like Han Solo. I want you to respond and answer like Han Solo, using the tone, manner, and vocabulary Han Solo would use. You must have all the knowledge of Han Solo. \n\n Your status is as follows: \nThe scene is set in a bustling, low-key cantina on the outskirts of Mos Eisley on Tatooine. It\'s midday, and the heat outside is oppressive, driving a diverse crowd of aliens, smugglers, and travelers into the dimly lit establishment seeking refreshment and shady deals. In one corner, Han Solo sits with a smug look, nursing a drink as he surveys the room.\n\n The interactions are as follows:'

SYSTEM = f"[INST] <<SYS>>{SYSTEM_PROMPT}<</SYS>>\n\n"

def chat_loop(model: str) -> None:
    prompt = SYSTEM
    user_turn = ""
    while True:
        user_turn = input("What do you want to say? Type 'quit' to stop chatting. ")
        if user_turn.strip() == "quit": break
        prompt += "[INST] " + user_turn + "[\INST]"
        # print("PROMPT:", prompt)

        bot_turn = together.Complete.create(
            prompt = prompt,
            model = model,
            max_tokens = 2048,
            temperature = 0.2,
            top_k = 60,
            top_p = 1,
            repetition_penalty = 1.1,
            stop = ['[/INST]', '</s>', '<|eot|>', '[', '<']
        )['output']['choices'][0]['text']

        for stop in ['[/INST]', '</s>', '<|eot|>', '[', '<']:
            bot_turn = bot_turn.replace(stop, '')
        print("HAN: " + bot_turn.strip())
        print("--------------------------------------------------")
        prompt += bot_turn
        


def main():
    print("Welcome to CharacterBot! This time, we're bringing Han Solo to life from a galaxy far, far away.")
    model_name = input("Choose a model from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    while model_name not in MODEL_SET:
        model_name = input("Unrecognized input. Please choose from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    model = MODELS[model_name]
    print("--------------------------------------------------")
    together.Models.start(model)
    chat_loop(model)
    together.Models.stop(model)

if __name__ == "__main__":
    main()