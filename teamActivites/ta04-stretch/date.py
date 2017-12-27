"""
CS241 Team Activity 4 - Stretch 
Written by Chad Macbeth
"""

class Date:
   ### Initialize the Date object
   def __init__(self):
      self.day = 1
      self.month = 1
      self.year = 2000

   ### Prompt the user for the date
   ### If an invalid date is entered, the user will be reprompted
   def prompt(self):
      valid_date = False  
      # Keep prompting until valid_date becomes true
      while not valid_date:
         self.day = int(input("Day: "))
         self.month = int(input("Month: "))
         self.year = int(input("Year: "))
         # Check the date and update the valid_date variable
         # Display an error message if needed
         valid_date = self.check_date()
         if not valid_date:
            print("Invalid entry.")
            print()

   ### Display the date
   def display(self):
      # :02d == format this a decimal with 2 digits, padding with 0
      print("{:02d}/{:02d}/{}" .format(self.month, self.day, self.year))

   ### Check for a valid date
   def check_date(self):
      if (self.month < 1 or self.month > 12):
         return False 
      if (self.year < 2000):
         return False
      return True 

   ### Display the date in long format
   def display_long(self):
      # Determine the month name
      if (self.month == 1):
         month_name = "January"
      elif (self.month == 2):
         month_name = "February"
      elif (self.month == 3):
         month_name = "March"
      elif (self.month == 4):
         month_name = "April"
      elif (self.month == 5):
         month_name = "May"
      elif (self.month == 6):
         month_name = "June"
      elif (self.month == 7):
         month_name = "July"
      elif (self.month == 8):
         month_name = "August"
      elif (self.month == 9):
         month_name = "September"
      elif (self.month == 10):
         month_name = "October"
      elif (self.month == 11):
         month_name = "November"
      elif (self.month == 12):
         month_name = "December"
      else:
         month_name = ""

      print("{} {:02d}, {}" .format(month_name, self.day, self.year))
   

