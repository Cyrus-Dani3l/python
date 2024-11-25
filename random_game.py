import random

def play_guessing_game():

    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_guessing_game()