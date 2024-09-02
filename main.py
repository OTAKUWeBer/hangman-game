from words import words
from hang_man_visual import lives_visual_dict
import random
import string
import os
import subprocess

def clear_screen():
    if os.name == 'nt':  # For Windows
        subprocess.run(['cls'], shell=True)
    else:  # For Unix/Linux/Mac
        subprocess.run(['clear'])
clear_screen()

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # Display used letters
        print(f'You have used these letters: {", ".join(used_letters)}')
        
        # Display current progress
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))
        
        # Getting user input
        user_input = input("Guess a letter (or multiple letters): ").upper()
        clear_screen()
        
        for user_letter in user_input:
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                    print(f"Correct guess for '{user_letter}'!")
                
                else:
                    lives -= 1
                    print(f"Incorrect guess for '{user_letter}'. You have {lives} lives left.")
            
            elif user_letter in used_letters:
                print(f"You've already guessed '{user_letter}'.")
            
            else:
                print(f"'{user_letter}' is an invalid character.")
        
        print()  # Add a blank line for readability between rounds
    
    if lives == 0:
        print(lives_visual_dict[lives])
        print(f"You died! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word: {word}")

if __name__ == "__main__":
    hangman()
