"""
CS241 Team Activity 1  
Written by Chad Macbeth
"""

dna_seq = input("Please enter your DNA sequence: ")

# Use a for loop to count the number of 'A'
count_a = 0
for dna in dna_seq:  # Will look at each character one a time
   if dna == "A":    # Could also do 'A'
      count_a += 1

print("The sequence {} has {} A's." .format(dna_seq, count_a))
print()

friend_dna_seq = input("Please enter your friends DNA sequence: ")

match = 0
# Deterimne shortest dna sequence
# If we don't do this, then we do an array out of bounds later
if len(dna_seq) < len(friend_dna_seq):  
   min_length = len(dna_seq)
else:
   min_length = len(friend_dna_seq)

for i in range(min_length):     # Will loop through all numbers from 0 to min_length-1
   if dna_seq[i] == friend_dna_seq[i]:
       match += 1
match_percent = (match / min_length) * 100.0

print("You and your friend had {} matches for {}%" .format(match, match_percent))


