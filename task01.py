import random
WORD_LIST = ["lived", "trees", "power", "shows", "wrote"]

def play_wordle():
    secret_word = random.choice(WORD_LIST).upper()
    attempts = 0
    max_attempts = 6

    print("Welcome to Simple Wordle!")
    print("Guess the 5-letter word in 6 tries.")
    print("---------------------------------")
    print(f"Hint: The word is one of {WORD_LIST}")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ").upper()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        if guess == secret_word:
            print(f" You won! The word was '{secret_word}'.")
            return

        feedback = ""
        for i in range(5):
            if guess[i] == secret_word[i]:
                feedback += "🟩"  
            elif guess[i] in secret_word:
                feedback += "🟨" 
            else:
                feedback += "⬜" 


import random
from colorama import Fore, Style, init

init(autoreset=True)
WORD_LIST = ["three", "again", "small", "never", "hello", "world","night"]

def play_wordle():
  
    secret_word = random.choice(WORD_LIST).upper()
    attempts = 0
    max_attempts = 6

    print("Welcome to Wordle! 🎮")
    print("Guess the 5-letter word in 6 attempts.")
    print("---------------------------------------")

    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ").upper()
        
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
            
        if guess == secret_word:
            print(Fore.GREEN +" Congratulations! The word was {secret_word}'.")
            return
        
        feedback = ""
        temp_secret = list(secret_word)
        temp_guess = list(guess)

        for i in range(5):
            if temp_guess[i] == temp_secret[i]:
                feedback += Fore.GREEN + temp_guess[i] + Style.RESET_ALL
                temp_secret[i] = None
            else:
                feedback += " "
        for i in range(5):
            if feedback[i] == " ":
                if temp_guess[i] in temp_secret:
                    feedback = feedback[:i] + (Fore.YELLOW + temp_guess[i] + Style.RESET_ALL) + feedback[i+1:]
                    temp_secret[temp_secret.index(temp_guess[i])] = None
                else:
                    feedback = feedback[:i] + (Fore.LIGHTBLACK_EX + temp_guess[i] + Style.RESET_ALL) + feedback[i+1:]
        
        print(f"Feedback: {feedback}")
        attempts += 1
            
    print(Fore.RED +" You ran out of attempts! The correct word was '{secret_word}'.")

if __name__ == "__main__":
    play_wordle()