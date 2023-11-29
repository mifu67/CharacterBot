"""
Main file for CharacterBot
"""

MODEL_SET = set(['young', 'regular', 'old'])
YOUNG = "mifu67@stanford.edu/llama-2-7b-chat-young-han-new-data-6--1e-05-2023-11-22-21-56-35"
REGULAR = "mifu67@stanford.edu/llama-2-7b-chat-han-first-3--1e-05-2023-11-24-05-56-02"
OLD = "mifu67@stanford.edu/llama-2-7b-chat-old-han-second-10--1e-05-2023-11-25-22-27-37"


def chat_loop(model: str) -> None:
    pass

def main():
    print("Welcome to CharacterBot! This time, we're bringing Han Solo to life from a galaxy far, far away.")
    model = input("Choose a model from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    while model not in MODEL_SET:
        model = input("Unrecognized input. Please choose from 'YOUNG', 'REGULAR', or 'OLD': ").strip()
    chat_loop(model)

if __name__ == "__main__":
    main()