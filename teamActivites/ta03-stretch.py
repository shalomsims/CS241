"""
CS241 Team Activity 03 - Stretch
Written by Chad Macbeth
"""

class Real:
 
   ### Initialize a Real number
   def __init__(self):
      self.numerator = 0
      self.denominator = 1

   ### Display the real number
   def display(self):
      # Check for improper fraction
      if self.numerator > self.denominator:
         # Perform integer division using //
         whole_number = self.numerator // self.denominator 
         new_numerator = self.numerator - (whole_number * self.denominator)
         print("{} {}/{}" .format(whole_number, new_numerator,
                                  self.denominator))
      else:
         print("{}/{}" .format(self.numerator, self.denominator))

   ### Prompt for the real number
   def prompt(self):
      self.numerator = int(input("Enter the numerator: "))
      self.denominator = int(input("Enter the denominator: "))

   ### Display the real number as a decimal
   def display_decimal(self):
      decimal = self.numerator / self.denominator
      print(decimal)

   ### Reduce the real number
   def reduce(self):
      # Find the greatest common divisor for both
      # the numerator and denominator
      gcd = 1

      # Use the min function since we don't know if the 
      # numerator or denominator is bigger.  The loop will 
      # run from 1 to the min(numerator, denominator) looking
      # for the largest common factor.
      for factor in range(1,min(self.numerator, self.denominator)+1):
         # Check if we found a number that divides both
         # the numerator and denominator evenly.
         if ((self.numerator % factor == 0) and
            (self.denominator % factor == 0)):
            gcd = factor
      # Divide numerator and denominator by the gcd to reduce
      self.numerator //= gcd 
      self.denominator //= gcd 

   ### Multiply two Real Number
   def multiply_by(self, real):
      self.numerator *= real.numerator
      self.denominator *= real.denominator

### Driver 
def main():
   real = Real()
   real.display()
   real.prompt()
   real.display()
   real.display_decimal()
   real.reduce()
   real.display()
   real2 = Real()
   real2.prompt()
   real2.display()
   real.multiply_by(real2)
   real.display()
   real.reduce()
   real.display()

if __name__ == "__main__":
   main()
   

