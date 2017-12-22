"""
CS241 Team Activity 3  
Written by Chad Macbeth
"""

class Real:
 
   ### Initialize a Real number
   def __init__(self):
      self.numerator = 0
      self.denominator = 1

   ### Display the real number
   def display(self):
      print("{}/{}" .format(self.numerator, self.denominator))

   ### Prompt for the real number
   def prompt(self):
      self.numerator = int(input("Enter the numerator: "))
      self.denominator = int(input("Enter the denominator: "))

   ### Display the real number as a decimal
   def display_decimal(self):
      decimal = self.numerator / self.denominator
      print(decimal)

### Driver 
def main():
   real = Real()
   real.display()
   real.prompt()
   real.display()
   real.display_decimal()

if __name__ == "__main__":
   main()
   

