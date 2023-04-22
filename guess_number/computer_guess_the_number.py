from random import randint

def computer_guess_number(final_limit_value: int, guess: int):
    random_number = randint(1, final_limit_value)
    while random_number != guess:
        print(f"Try to hit a number between 1 and {guess}")
        if random_number < guess:
            print("Sorry, you're wrong. Try again too low!")
            break
        elif random_number > guess:
            print("Sorry, you're wrong. Try again too high!")
            break
        else:
            print(f"Congrats! You're right.")
            break

if __name__ == '__main__':
    final_limit_value = randint(1, 1000)
    guess = randint(1, final_limit_value)
    computer_guess_number(final_limit_value, guess)