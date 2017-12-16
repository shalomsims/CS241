"""
CS241 Checkpoint 01B - Input/Output 
Written by Chad Macbeth
"""

name = input("Please enter your name: ")
age_str = input("Please enter your age: ")
age = int(age_str)

print()
print("Hello {}, you are {} years old." .format(name,age))
print("On your next birthday, you will be {}." .format(age+1))


