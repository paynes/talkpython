import random

print('------------------------------')
print('    GUESS THAT NUMBER GAME')
print('------------------------------')

the_number = random.randrange(0, 101)
guess_number = -1

while guess_number != the_number:
	guess_number = input('Guess a number between 0 and 100: ')
	guess_number = int(guess_number)

	if guess_number > the_number:
		print(f'{guess_number} is HIGHER than secret number.')
	elif guess_number < the_number:
		print(f'{guess_number} is LOWER than secret number.')
	else:
		print(f'{guess_number} is the secret number. You win!!!')
