import random

def guess(x):
	random_number = random.randint(1,x)
	guess=0
	while guess != random_number:
		guess = int(input(f'Guess a number between 1 and {x}: '))
		if guess < random_number:
			print('Sorry, guess again ... Too low.')
		elif guess > random_number:
			print('Sorry, guess again ... Too high.')
		
	print(f'Yay, Congrats. You have guessed the number {random_number}')

def computer_guess(x):
	low=1
	high=x
	feedback=''
	while feedback !='c':
		if low != high:
			guess = random.randint(low,high)
		else:
			guess = low #could be high as low = high
		feedback=input(f'Is {guess} to high (H), too low (L), or Correct (C)').lower()
		if feedback =='h':
			high=guess-1
		elif feedback =='l':
			low=guess+1

	print(f'The Computer Guessed  Your Number, {guess}, Correctly!')

print('1. Guess The Number (computer)\n2. Guess The Number (user)')
choice = int(input())
if choice == 1:
	guess(10)
elif choice ==2:
	computer_guess(10)