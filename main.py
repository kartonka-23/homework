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

# num = random.randint(1, 10)
# y = 3
# for i in range(3):
# 	y -= 1
# 	answ = int(input("write number between 1-10: "))
	
# 	if y == 0:
# 		print("You are losed")
# 		break
# 	else:
# 		print(f"you have {y} tries")

# 	if answ < num:
# 		print("greater number")
# 	elif answ > num:
# 		print("smaller number")
# 	elif answ == num:
# 		print("You are guessed")
# 		break
# 	i += 1





# min_num = int(input("enter smaller number: "))
# max_num = int(input("enter larger number: "))
# norm_num = max_num - 1


# while min_num != norm_num:
# 	min_num+=1
# 	print(min_num)





# task 5
# start_num = int(input("enter any number: "))
# a = -1
# while a != start_num:
	
# 	if a < start_num:
# 		a += 2
# 		print(a)
# 	elif a > start_num:
# 		break





# task 6
n = int(input("Enter the number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("factorial:", factorial)
