import random


def guess(x):
    random_no = random.randint(1, x)
    guess = 0
    while guess != random_no:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_no:
            print("Too low for the number!")
        elif guess > random_no:
            print("Too high for the number!")
    print(f"you got the number {random_no} right!")

#guess(13)


def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        #guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), ir correct (C)?")
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f"The computer guessed the number {guess} correctly!")
    comp_guess(10)