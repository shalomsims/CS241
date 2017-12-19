"""
CS241 Team Activity 2  
Written by Chad Macbeth
"""

### Prompt the user to provide a filename
def prompt_filename():
   filename = input("Enter filename: ")
   return filename

### Parse each word from the file
def parse_file(filename):
   count = 0
   file_in = open(filename, "r")
   for line in file_in:    # Read each line in the file
      words = line.split() # Default is spaces
      for word in words:   # Read each word in the line
         if word == "pride":
            count += 1
   file_in.close()
   return count

### Driver 
def main():
   filename = prompt_filename()
   print("Opening file {}" .format(filename))
   count = parse_file(filename)
   print("The word pride occurs {} times in this file." .format(count))

if __name__ == "__main__":
   main()
   

