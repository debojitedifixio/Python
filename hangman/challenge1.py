import random                                               # importing the module random
import hangman_art                                          # importing the file as module hangman_art
import hangman_words                                        # importing the file as module hangman_words


lives = 6                                   # assigning the live count to display hangman
print(hangman_art.logo)                     # printing the hangman logo
chosen_word = random.choice(hangman_words.word_list)    # assigning the random word from word_list

print(f"Psst, the chosen word is {chosen_word}")        # showing the random words

display = []                                            # creating an empty list
end_of_game = False
word_length = len(chosen_word)

# Loop for storing the word in the list and joining them
for letter in chosen_word:
    display.append("_")
print(f"{' '.join(display)}")

# Loop for the whole program checking the while value
while not end_of_game:
    guess = input("Guess a letter: ").lower()  # taking inputs from the user

    # Loop for the repeating guessed letter
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    # loop for placing the guessed letter in the correct position
    for position in range(0, word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # loop for the wrong word chosen
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives - 1                   # decrementing the lives
        print(hangman_art.stages[lives])    # printing the hangman ascii
        # loop for ending the game when lives = 0
        if lives == 0:
            end_of_game = True
            print("You Lose.")
    print(f"{' '.join(display)}")
    # loop to end the game when user chose all words correctly and no more _ left
    if "_" not in display:
        end_of_game = True
        print("You win.")