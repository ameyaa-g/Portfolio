# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Ameya Gopinath
# Section:      M02
# Assignment:   Lab 9
# Date:         11 10 2023


# assigned the secret number
secret_number = 27
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
flag = False
count = 0
# compare the guess and the secret number
def compare(guess, secret_number, count):
    if guess < secret_number:
        print('Too low!')
    elif guess > secret_number:
        print('Too high!')
    elif guess == secret_number:
        print(f'You guessed it! It took you {count} guesses.')

# check if guess is a valid number
def is_valid(tguess):

     while (True):

        if '.' not in tguess:
            try:
                tguess = int(tguess)
                break
            except ValueError:
                pass
        tguess = input('Bad input! Try again:')
        continue

     return tguess

# get the input number
def get_input(tcount):
    tguess = input('What is your guess?')
    tcount += 1
    return tcount, tguess

# while the guess is not the secret number, keep looping
while flag != True:

    count, guess = get_input(count)
    guess = is_valid(guess)

    compare(guess, secret_number, count)

    if guess == secret_number:
        flag = True


