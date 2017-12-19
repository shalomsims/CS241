"""
CS241 Checkpoint 02B
Written by Chad Macbeth
"""

### Get file name from the user
def get_filename():
   filename = input("Enter file: ")
   return filename

### Open the file and analyze words and lines
### Returns a tuple (word count, line count)
def read_file(filename):
   file_in = open(filename, "r")
   line_count = 0 
   word_count = 0
   for line in file_in:        # Loop through each line of the file
      line_count += 1
      words = line.split()     # Create a list of words from the line (default is spaces) 
      word_count += len(words) # Count the number of words in the list 
   file_in.close()
   return (word_count, line_count)

### Driver to test funtions
def main():
   filename = get_filename()
   (word_count, line_count) = read_file(filename)
   print("The file contains {} lines and {} words." .format(line_count, word_count))

if __name__ == "__main__":
   main()



