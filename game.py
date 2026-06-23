import random

def start_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Game Start! 1 se 100 ke beech guess karo.")

    while True:
        try:
            guess = int(input("Guess karo: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f"Sahi jawab! Attempts: {attempts}")
                break
        except ValueError:
            print("Sirf number enter karo.")

if __name__ == "__main__":
    start_game()