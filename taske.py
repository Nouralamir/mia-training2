import random
from collections import Counter

# A small list of 5-letter words for the game.
# You can easily expand this list with more words.
WORDS = [
    "APPLE", "BRAVE", "CRANE", "DRIVE", "EQUAL", "FROST", 
    "GHOST", "HOUSE", "IDEAS", "JUICE", "KNIFE", "LUCKY",
    "MAGIC", "NIGHT", "OCEAN", "POWER", "QUITE", "ROBOT",
    "SPACE", "TIGER", "UNITY", "VOICE", "WATER", "XENON", 
    "YACHT", "ZEBRA"
]

def check_guess(secret_word, guess):
    """
    Compares a guess to a secret word and returns feedback for each letter.
    The feedback is a list of tuples, where each tuple contains the letter
    from the guess and its status.

    - 'correct': The letter is in the secret word and in the correct position.
    - 'present': The letter is in the secret word but in a different position.
    - 'absent': The letter is not in the secret word at all.
    
    Args:
        secret_word (str): The word the player is trying to guess.
        guess (str): The word the player has guessed.
    
    Returns:
        list: A list of tuples containing (letter, status) for each letter in the guess.
    """
    # Create a frequency map of letters in the secret word
    secret_letter_counts = Counter(secret_word)
    result = [(letter, 'absent') for letter in guess]

    # First pass: Find 'correct' letters
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result[i] = (guess[i], 'correct')
            secret_letter_counts[guess[i]] -= 1

    # Second pass: Find 'present' letters
    for i in range(len(guess)):
        if result[i][1] != 'correct':
            if secret_letter_counts.get(guess[i], 0) > 0:
                result[i] = (guess[i], 'present')
                secret_letter_counts[guess[i]] -= 1
    
    return result

def print_feedback(feedback):
    """
    Prints the guess feedback in a user-friendly format for the command line.
    
    - '*' indicates a 'correct' letter.
    - '+' indicates a 'present' letter.
    - '-' indicates an 'absent' letter.
    """
    display_string = ""
    for letter, status in feedback:
        if status == 'correct':
            display_string += f"[{letter}:*] "
        elif status == 'present':
            display_string += f"[{letter}:+] "
        else: # status == 'absent'
            display_string += f"[{letter}:-] "
    print(display_string)

def main():
    """
    The main function to run the Wordle game.
    """
    print("Welcome to Command-Line Wordle!")
    print("You have 6 attempts to guess a 5-letter word.")
    print("Feedback will be given for each letter in your guess:")
    print("  - [*] means the letter is correct and in the right position.")
    print("  - [+] means the letter is correct but in the wrong position.")
    print("  - [-] means the letter is not in the word.")
    print("-" * 30)

    # Choose a random secret word from the list and convert to uppercase.
    secret_word = random.choice(WORDS).upper()
    
    num_guesses = 0
    max_guesses = 6
    has_won = False

    while num_guesses < max_guesses:
        guess = input(f"Guess #{num_guesses + 1} (5 letters): ").upper()

        # Basic input validation
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in WORDS and guess != secret_word:
            print("That word is not in our word list. Please try again.")
            continue
        
        num_guesses += 1
        
        feedback = check_guess(secret_word, guess)
        print_feedback(feedback)
        
        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {num_guesses} attempts.")
            has_won = True
            break