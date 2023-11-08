"""
Uses the fandom-py library to fetch data necessary for grounding
"""

import fandom
import os

def fetch_data(character: str)-> None:
    fandom.set_wiki("Wookieepedia")
    try:
        backstory = fandom.page(character)
        print("Relevant page found!")
    except fandom.error.PageError:
        print("Sorry, it seems like we couldn't find that character in Wookieepedia. Please try again.")
        return
    
    # if this is the first time using characterbot, we need to create a new "data" directory
    try:
        os.mkdir("data")
        print("Created data folder.")
    except FileExistsError:
        print("Data directory found, skipping folder creation.")

    # get the filename from the full character name
    fname = "data/" + ''.join(character.split()).lower() + ".txt"
    f = open(fname, "w")
    # write formatted plain text to file
    print(backstory.plain_text, file=f)
    f.close()