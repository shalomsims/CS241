"""
CS241 Checkpoint 01B 
Written by Chad Macbeth
"""

# The input command only returns a string
# We must convert this to integer if needed

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print()   # Prints a blank line (can also do \n)
print("Hello {}, you are {} years old." .format(name,age))
print("On your next birthday, you will be {}." .format(age+1))


