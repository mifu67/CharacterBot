"""
Uses the fandom-py library to fetch data necessary for grounding.
"""

import fandom
import os

from typing import List

def fetch_data(characters: List[str])-> None:
    fandom.set_wiki("Wookieepedia")
    # if this is the first time using characterbot, we need to create a new "raw_data" directory
    try:
        os.mkdir("raw_data")
        print("Created data folder.")
    except FileExistsError:
        print("Data directory found, skipping folder creation.")

    for character in characters:
        try:
            backstory = fandom.page(character)
            print("Relevant page found!")
        except fandom.error.PageError:
            print("Sorry, it seems like we couldn't find " + character + " in Wookieepedia. Please try again.")
            continue

        # get the filename from the full character name
        fname = "raw_data/" + ''.join(character.split()).lower() + ".txt"
        f = open(fname, "w")
        # write formatted plain text to file
        print(backstory.plain_text, file=f)
        f.close()

def main():
    characters = ["Han Solo", "Leia Organa Solo", "Anakin Skywalker", "Obi-Wan Kenobi", "Yoda"]
    # you'll get a keyerror on this page when using fandom-py 
    # I changed the get_section function somewhat to get this text; just use the provided file for simplicity
    characters = ["Luke Skywalker"] 
    fetch_data(characters)

if __name__ == "__main__":
    main()