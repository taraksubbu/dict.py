import random

while True:
	d=input("press r to roll,q to quit.")

	if d == 'r':
		print(random.radiant(1,6))

	elif d == 'q':
		print("Bye!")
		exit()

	print("End!")
