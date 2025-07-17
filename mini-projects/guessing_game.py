import random

# Step 1: Pick a secret number
secret_number = random.randint(1, 100)  # Secret number between 1 and 100

# Step 2: Set up the game loop
guesses_taken = 0
while True:
    # Step 3: User input
    guess = int(input("Guess the secret number (between 1 and 100): "))
    guesses_taken += 1
    
    # Step 4: Provide feedback
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"\nCongratulations! You guessed it in {guesses_taken} tries.")
        break  # Exit the loop when the correct number is guessed
