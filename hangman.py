import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer", "keyboard", "game"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed = ""
    for letter in word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6 

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            all_guessed = True
            for letter in word:
                if letter not in guessed_letters:
                    all_guessed = False
                    break
            if all_guessed:
                print(f"Congratulations! You guessed the word: {word}")
                break
        else:
            print("Incorrect guess.")
            attempts -= 1

    if attempts == 0:
        print(f"Game over! The word was: {word}")

hangman()
