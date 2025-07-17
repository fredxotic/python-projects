import random

# Step 1: Word list
word_list = ["python", "hangman", "developer", "program", "keyboard"]
chosen_word = random.choice(word_list)

# Step 2: Game variables
guessed_letters = []
tries = 6
display_word = ["_" for _ in chosen_word]

# Step 3: Game loop
while tries > 0 and "_" in display_word:
    print("\nCurrent word: ", " ".join(display_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

# Step 4: End of game
if "_" not in display_word:
    print("\nYou guessed the word:", chosen_word)
    print("🎉 You win!")
else:
    print("\nOut of tries! The word was:", chosen_word)
    print("💀 Game over!")
