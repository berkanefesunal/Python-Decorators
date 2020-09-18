


import random
number=random.randint(1,100)
win=False
Turns=0
while win == False:
	guess=input('Enter a number')
	turns +=1
	if number=int(guess):
		print('you won')
		print('you played',turns)
		win=True
		break
	else:
	if number> int(guess):
		print('you are sooooo low dudeeeeee')
	else:
		print('you are sooooo highh dudeeeeeee')
		
