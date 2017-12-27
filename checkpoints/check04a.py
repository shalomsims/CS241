"""
CS241 Checkpoint 4A 
Written by Chad Macbeth
"""

class Person:

   ### Initialize a Person object
   def __init__(self):
      self.name = "anonymous"
      self.year = "unknown"

   ### Display a person
   def display(self):
      print("{} (b. {})" .format(self.name, self.year))

class Book:

   ### Initialize a Book object
   def __init__(self):
      self.title = "untitled"
      self.author = Person()
      self.publisher = "unpublished"

   ### Display a Book
   def display(self):
      print(self.title)
      print("Publisher:")
      print(self.publisher)
      print("Author:")
      self.author.display() # Call the display function in the Person class

### Test the classes
def main():
   book = Book()
   book.display()
   print()
   print("Please enter the following:")
   book.author.name = input("Name: ")
   book.author.year = input("Year: ")
   book.title = input("Title: ")
   book.publisher = input("Publisher: ")
   print()
   book.display() 

if __name__ == "__main__":
   main()



