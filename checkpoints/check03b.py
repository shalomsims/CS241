"""
CS241 Checkpoint 3B 
Written by Chad Macbeth
"""

class Complex:

   ### Initialize a Complex number
   def __init__(self):
      self.real = 0 
      self.imaginary = 0

   ### Prompt the user for a complex number
   def prompt(self):
      self.real = int(input("Please enter the real part: "))
      self.imaginary = int(input("Please enter the imaginary part: "))

   ### Display the complex number
   def display(self):
      print("{} + {}i" .format(self.real, self.imaginary))
      

### Driver for testing
def main():
   c1 = Complex()
   c2 = Complex()
   print("The values are:")
   c1.display()
   c2.display()
   print()
   c1.prompt()
   print()
   c2.prompt()
   print()
   print("The values are:")
   c1.display()
   c2.display()

if __name__ == "__main__":
   main()



