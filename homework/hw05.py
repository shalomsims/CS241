"""
CS241 Homework 05
Written by Chad Macbeth
"""

filename = input("File: ")
fileIn = open(filename, "r")
braces = []
balanced = True
for brace in fileIn:
   brace = brace.strip() # Remove whitespace
   if (brace == "{") or (brace == "(") or (brace == "["):
      braces.append(brace)  # Push open brace onto the stack
   else:
      if (len(braces) == 0): # Close brace received but empty stack
         balanced = False
         break
      # Pop off stack and check for mismatch between open and close brace
      prev_brace = braces.pop()
      if (((brace == "}") and (prev_brace != "{")) or
          ((brace == ")") and (prev_brace != "(")) or
          ((brace == "]") and (prev_brace != "["))):
         balanced = False
         break   

fileIn.close
# Stack should now be empty.  If it is not, then not balanced.
if (len(braces) != 0) or (not balanced):
   print("Not balanced")
else:
   print("Balanced")
