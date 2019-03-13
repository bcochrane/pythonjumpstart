import random

print('--------------------------')
print('  GUESS THAT NUMBER GAME')
print('--------------------------')
print()

player_name = input('What is your name? ')

the_number = random.randint(0, 100)
guess = -1
guess_count = 0

while guess != the_number:
    guess_str = input('Guess a number from 0 to 100: ')
    guess = int(guess_str)

    guess_count += 1

    if guess < the_number:
        print(f'Sorry, {player_name}. Your guess was too low.')
    elif guess > the_number:
        print(f'Sorry, {player_name}. Your guess was too high.')
    else:
        print(f'Congratulations, {player_name}! You correctly guessed the number ({the_number}). It took you {guess_count} guess(es).')
