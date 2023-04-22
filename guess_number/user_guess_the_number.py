from random import randint

def user_guess_number(final_limit_value: int, guess:int) -> None:
    random_number = randint(1, final_limit_value)
    user_number = int(input("Enter with your random number: "))
    while random_number != user_number:
        print(f"Try to hit a number between 1 and {final_limit_value}")
        if random_number < user_number:
            print("Sorry, you're wrong. Try again too low!")
            break
        elif random_number > user_number:
            print("Sorry, you're wrong. Try again too high!")
            break
        else:
            print(f"Congrats! You're right.")
            break

if __name__ == '__main__':
    final_limit_value = int(input("Enter the final number in the interval between values: "))
    guess = randint(1, final_limit_value)
    user_guess_number(final_limit_value, guess)
