import random


# task 1-2

# print('''
# 							TASK 1
# 	''')
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# if age <= 17:
# 	print("sorry but you're too young")
# else:
# 	print(f"Hi {name}, you're {age} years old, entry is allowed")





# task 3

import random
num = random.randint(1, 10)
y = 3
for i in range(3):
	y -= 1
	answ = int(input("write number between 1-10: "))
	
	if y == 0:
		print("You are losed")
		break
	else:
		print(f"you have {y} tries")

	if answ < num:
		print("greater number")
	elif answ > num:
		print("smaller number")
	elif answ == num:
		print("You are guessed")
		break
	i += 1