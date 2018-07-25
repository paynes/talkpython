import random
import time

from actors import Creature, Wizard, SmallAnimal, Dragon


def main():
	print_header()
	game_loop()


def print_header():
	print('------------------------------')
	print('      WIZARD BATTLE APP')
	print('------------------------------')


def game_loop():
	creatures = [
		SmallAnimal('Toad', 1),
		Creature('Tiger', 12),
		SmallAnimal('Bat', 3),
		Dragon('Dragon', 50, 75, True),
		Wizard('Evil Wizard', 1000)
	]

	hero = Wizard('Gandalf', 75)

	while True:
		active_creature = random.choice(creatures)

		print(f'A {active_creature.name} of level {active_creature.level} has apper from a dark and foggy forest...')
		cmd = input('Do you [a]ttack, [r]unaway or [l]ook around? \n')

		if cmd == 'a':
			if hero.attack(active_creature):
				print(f'The Wizard won and killed {active_creature.name}.')
				creatures.remove(active_creature)
			else:
				print(f'{active_creature.name} won.')
				print('The Wizard runs and hides taking time to recover...')
				time.sleep(5)
				print('The Wizard returns revitalized!')
		elif cmd == 'r':
			print('The Wizard has become unsure of his power and flees!!!')
		elif cmd == 'l':
			print(f'The Wizard {hero.name} takes in the surroundings and sees:')
			for c in creatures:
				print(f'* A {c.name} of level {c.level}')
		else:
			print('OK, exiting game...bye!')
			break


if __name__ == '__main__':
	main()
