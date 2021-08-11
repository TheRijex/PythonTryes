import random
tries = 0
number = random.randint(1,50)

print('Try to guess what number between 1 and 50 I was thinking about')

while tries < 6:
    guess = int( input('Take a guess'))
    tries+=1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is to high')
    if guess == number:
        print(f'You guessed my number in {tries} guesses')
        break
    if guess != number and tries == 6:
        print(f"Sorry, but you didn't make it. My number is {number}")
        break
