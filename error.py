try:
	a=int(input("enter"))
	if a<=6:
		raise NameError
	else:
		raise TypeError

except NameError:
	print("err...error when a is equal to 6")
except TypeError:
	print("error occured when you have chosen less than 6")
else:
	print("no error")
finally:
	print("execution completed")