import random
import hangman_art
import hangman_words


lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

print(f"Psst, the chosen word is {chosen_word}")

display = []
end_of_game = False
word_length = len(chosen_word)

for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()  # c

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives - 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")









