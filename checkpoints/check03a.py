"""
CS241 Checkpoint 3A
Written by Chad Macbeth
"""

class Student:

   ### Initialize a Student
   def __init__(self):
      self.first_name = ""
      self.last_name = ""
      self.id = 0

### Prompt for a Student and return a Student object
def prompt_student():
   new_student = Student()
   new_student.first_name = input("Please enter your first name: ")
   new_student.last_name = input("Please enter your last name: ")
   # Combine the int and input commands into one
   new_student.id = int(input("Please enter your id number: "))
   return new_student

### Display information in a Student object
def display_student(curr_student):
   print("{} - {} {}" .format(curr_student.id, 
                              curr_student.first_name, 
                              curr_student.last_name))

### Driver to test funtions
def main():
   my_student = prompt_student()
   print()
   print("Your information:")
   display_student(my_student)

if __name__ == "__main__":
   main()



