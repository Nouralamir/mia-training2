import random
from collections import Counter

WORDS = [
    "apple", "point", "story", "DRIVE", "EQUAL", "would",
    "ghost", "after", "water", "frist", "which", "there",
    "asked", "while", "found", "small", "years", "after",
    "house", "below", "UNITY", "every", "think", "where"
]

def check_guess(secret_word, guess):
  
   
    secret_letter_counts = Counter(secret_word)
    result = [(letter, 'absent') for letter in guess]

 
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result[i] = (guess[i], 'correct')
            secret_letter_counts[guess[i]] -= 1

   
    for i in range(len(guess)):
        if result[i][1] != 'correct':
            if secret_letter_counts.get(guess[i], 0) > 0:
                result[i] = (guess[i], 'present')
                secret_letter_counts[guess[i]] -= 1
    
    return result

def print_feedback(feedback):
   
    feedback_emojis = {
        'correct': '🟩',
        'present': '🟨',
        'absent': '⬜'
    }
    
    display_string = ""
    for letter, status in feedback:
        display_string += f"{feedback_emojis[status]}{letter} "
    print(display_string)

def main():
   
    print("Welcome to Command-Line Wordle!")
    print("You have 6 attempts to guess a 5-letter word.")
    print("Feedback will be given for each letter in your guess:")
    print("  🟩 - Correct letter, correct position.")
    print("  🟨 - Correct letter, wrong position.")
    print("  ⬜ - Letter is not in the word.")
    print("-" * 30)


    secret_word = random.choice(WORDS).upper()
    
    num_guesses = 0
    max_guesses = 6
    has_won = False
    
    guess_history = []

    while num_guesses < max_guesses:
        guess = input(f"Guess #{num_guesses + 1} (5 letters): ").upper()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue
        if guess not in WORDS:
            print("That word is not in our word list. Please try again.")
            continue
        
        num_guesses += 1
        
        feedback = check_guess(secret_word, guess)
        guess_history.append((guess, feedback))

        print("\n--- Game State ---")
        for prev_guess, prev_feedback in guess_history:
            print(f"Guess: {prev_guess}")
            print_feedback(prev_feedback)
            print()
        print("-" * 30)
        
        if guess == secret_word:
            print(f"Congratulations! You guessed the word '{secret_word}' in {num_guesses} attempts.")
            has_won = True
            break
            
    if not has_won:
        print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")

if __name__ == "__main__":
    main()
