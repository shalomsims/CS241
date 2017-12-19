"""
CS241 Team Activity 2 - Stretch
Written by Chad Macbeth
"""

### Prompt the user to provide a filename
def prompt_filename():
   filename = input("Enter filename: ")
   return filename

### Prompt the user to provide a target word to search
def prompt_target():
   target = input("Enter target word to search: ")
   return target

### Parse each word from the file looking for the target word
def parse_file(filename, target):
   count = 0
   file_in = open(filename, "r")
   for line in file_in:     # Read each line in the file
      words = line.split()  # Default are spaes
      for word in words:    # Read each word in the line
         if word.upper().find(target.upper()) != -1:  # Look for substrings in uppercase
            count += 1
   file_in.close()
   return count

### Driver 
def main():
   filename = prompt_filename()
   target = prompt_target()
   print("Opening file {}" .format(filename))
   count = parse_file(filename, target)
   print("The word {} occurs {} times in this file." .format(target, count))

if __name__ == "__main__":
   main()
   

