import random

def hangman():
    words = ["python", "programming", "hangman", "challenge", "game", "past", "pygame"]
    word = random.choice(words).lower()
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")
    
    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print("Attempts left:", attempts)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        elif guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts -= 1
            print("Incorrect guess.")
    
    if "_" not in guessed_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nYou're out of attempts. The word was:", word)

hangman()
