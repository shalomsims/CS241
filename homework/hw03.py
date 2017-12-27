"""
CS241 Homework 03
Written by Chad Maceth
"""

# Start with empty lists
odd_numbers = []
even_numbers = []

# Loop until 0 is entered
number = 1
while (number != 0):
   number = int(input("Enter a number (0 to quit): "))
   # If number is even (and not 0) then add to even list
   # if number is odd then add to odd list
   if (number != 0 and number % 2 == 0):
      even_numbers.append(number)
   elif (number % 2 == 1):
      odd_numbers.append(number)

# Print out both lists

print()
print("Even numbers:")
for number in even_numbers:
   print(number)

print()
print("Odd numbers:")
for number in odd_numbers:
   print(number)
