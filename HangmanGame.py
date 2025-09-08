import random
def hangman_game():
    words = ['ankita', 'tiger', 'python', 'india', 'sahuji']
    word = random.choice(words)
    guessed = ['_'] * len(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print('Welcome to Hangman!')
    print('Guess the word:', ' '.join(guessed))

    while incorrect_guesses < max_incorrect and '_' in guessed:
        guess = input('Enter a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter exactly one alphabetic letter.')
            continue

        if guess in guessed_letters:
            print(f'You already guessed "{guess}". Try a different letter.')
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
            print('Good guess!')
        else:
            incorrect_guesses += 1
            print(f'Wrong guess! You have {max_incorrect - incorrect_guesses} guesses left.')

        print('Current word:', ' '.join(guessed))

    if '_' not in guessed:
        print(f'Congratulations! You guessed the word "{word}".')
    else:
        print(f'Sorry, you lost. The word was "{word}".')
hangman_game()
