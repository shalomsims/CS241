"""
CS241 Team Activity 4  
Written by Chad Macbeth
"""

class Date:
   ### Initialize the Date object
   def __init__(self):
      self.day = 1
      self.month = 1
      self.year = 2000

   ### Prompt the user for the date
   def prompt(self):
      self.day = int(input("Day: "))
      self.month = int(input("Month: "))
      self.year = int(input("Year: "))

   ### Display the date
   def display(self):
      print("{}/{}/{}" .format(self.month, self.day, self.year))
   
   

