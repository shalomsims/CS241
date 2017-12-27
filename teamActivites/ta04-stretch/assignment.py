"""
CS241 Team Activity 4 - Stretch
Written by Chad Macbeth
"""

from date import Date

class Assignment:
   ### Initialize the Date object
   def __init__(self):
      self.name = "Untitled"
      self.start_date = Date()
      self.due_date = Date()
      self.end_date = Date()

   ### Prompt for the assignment from the user
   def prompt(self):
      self.name = input("Name: ")
      print()
      print("Start Date:")
      self.start_date.prompt()
      print()
      print("Due Date:")
      self.due_date.prompt()
      print()
      print("End Date:")
      self.end_date.prompt()

   ### Display the assignment 
   def display(self):
      print("Assignment: {}" .format(self.name))
      print("Start Date:")
      self.start_date.display()
      self.start_date.display_long()
      print("Due Date:")
      self.due_date.display()
      self.due_date.display_long()
      print("End Date:")
      self.end_date.display()
      self.end_date.display_long()
   
   

