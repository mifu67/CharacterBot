"""
Main file for CharacterBot
"""
import together


MODEL_SET = set(['young', 'regular', 'old'])
YOUNG = "mifu67@stanford.edu/llama-2-7b-chat-young-han-new-data-6--1e-05-2023-11-22-21-56-35"
REGULAR = "mifu67@stanford.edu/llama-2-7b-chat-han-first-3--1e-05-2023-11-24-05-56-02"
OLD = "mifu67@stanford.edu/llama-2-7b-chat-old-han-second-10--1e-05-2023-11-25-22-27-37"

SYSTEM_PROMPT = 'I want you to act like Han Solo. I want you to respond and answer like Han Solo, using the tone, manner, and vocabulary Han Solo would use. You must have all the knowledge of Han Solo. \n\n Your status is as follows: \nThe scene is set in a bustling, low-key cantina on the outskirts of Mos Eisley on Tatooine. It\'s midday, and the heat outside is oppressive, driving a diverse crowd of aliens, smugglers, and travelers into the dimly lit establishment seeking refreshment and shady deals. In one corner, Han Solo sits with a smug look, nursing a drink as he surveys the room.\n\n The interactions are as follows:'

SYSTEM = f"[INST] <<SYS>>{SYSTEM_PROMPT}<</SYS>>\n\n"

def chat_loop(model: str) -> None:
    prompt = SYSTEM
    user_turn = ""
    while user_turn.strip() != 'quit':
        user_turn = input("What do you want to say? Type 'quit' to stop chatting.")
        prompt += "[INST] " + user_turn

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
        print(bot_turn)
        prompt += "[/INST] " + bot_turn


def main():
    print("Welcome to CharacterBot! This time, we're bringing Han Solo to life from a galaxy far, far away.")
    model = input("Choose a model from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    while model not in MODEL_SET:
        model = input("Unrecognized input. Please choose from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    print("--------------------------------------------------")
    chat_loop(model)

if __name__ == "__main__":
    main()