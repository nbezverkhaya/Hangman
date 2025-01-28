import random
from Hangman_art import stages, logo
from Hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

print(logo)

display = ["_" for _ in range(word_length)]
print(f"{' '.join(display)}")
print()

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")
        continue
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

