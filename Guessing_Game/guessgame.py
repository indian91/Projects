import time
from random import randint
print('*'*80)
print('*'*80)
print()
print('** Welcome to Guessing Game **'.center(80))
print()
print('*'*80)
print('*'*80)
print()
time.sleep(1)
print('Computer Guessing a Number.....')
com=randint(1,50)
time.sleep(1)
print()
print('Guess the Number in Five Chances')
chance=1
while chance <= 5:
    print()
    user=int(input('Enter a number between 1-50 only: '))
    if user<1 or user > 50:
        continue
    elif user<com:
        print('Think Big')
    elif user>com:
        print('Think Lower')
    elif user==com:
        print('Congratulations........')
        time.sleep(.5)
        print('You have won the Game')
        break
    print(f'Chance Remaining: {5-chance}')
    chance+=1
else:
    print('Chance Over')
    print()
    print('You are such a looser.....')
    print()
    print(f'Computer guess was {com}')
