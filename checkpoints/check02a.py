"""
CS241 Checkpoint 02A 
Written by Chad Macbeth
"""

### Prompt for a positive number from the user.
def prompt_number():
   number = -1
   while number < 0:
      number_str = input("Enter a positive number: ")
      number = int(number_str)
      if number < 0:
         print("Invalid entry. The number must be positive.")
   print()
   return number

### Add 3 numbers
def compute_sum(number1, number2, number3):
   return (number1 + number2 + number3)

### Driver to test funtions
def main():
   num1 = prompt_number()
   num2 = prompt_number()
   num3 = prompt_number()
   sum = compute_sum(num1, num2, num3)
   print("The sum is: {}" .format(sum))

if __name__ == "__main__":
   main()



