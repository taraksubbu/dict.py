
for i in range(1,7):
	r = ("press r to roll, q to quit")

	if r == "r":
		if i == 1 or i == 3 or i == 4:
			print("you got ",6)

		elif i == 2 or i == 5:
			print("you got",2)
		else:
		    print("you got",3)
	elif r == "q":
	   print("Bye!")
	   exit()
print("Hurray, you won!")