"""
CS241 Team Activity 1 - DNA 
Written by Chad Macbeth
"""

dna_seq = input("Please enter your DNA sequence: ")

# Core 1: Count the number of A's

count_a = 0
for dna in dna_seq:
   if dna == "A":
      count_a += 1

print("The sequence {} has {} A's." .format(dna_seq, count_a))
print()

# compareDna will return [number of matches , percent match]
def compare_dna(dna, friend_dna):
   match = 0
   if len(dna) < len(friend_dna):  # Determine shortest length
      min_length = len(dna)
   else:
      min_length = len(friend_dna)
   for i in range(min_length):     # Count matches
      if dna[i] == friend_dna[i]:
          match += 1
   match_percent = (match / min_length) * 100.0
   return [match, match_percent]
#### END DEF

# Core 2/3: Compare DNA

dna_seq_friend = input("Please enter your friend's DNA sequence: ")
result = compare_dna(dna_seq, dna_seq_friend)
print("You and your friend had {} matches for {}%" .format(result[0], result[1]))
print()

# Stretch: 

# Get the number of friends
num_friends_str = input("How many friends: ")
num_friends = int(num_friends_str)

# Get the friend names
friend_name_list = []
for i in range(num_friends):
   friend_name = input("Please enter your friend #{} name: " .format(i+1))
   friend_name_list.append(friend_name)

# Get the friend DNA
friend_dna_seq_list = []
for i in range(num_friends):
   friend_dna_seq = input("Enter the DNA sequence for {}: " .format(friend_name_list[i]))
   friend_dna_seq_list.append(friend_dna_seq)

# Display match results
for i in range(num_friends):
   result = compare_dna(dna_seq, friend_dna_seq_list[i])
   print("You and your friend {} had {} matches for {}%" .format(friend_name_list[i], result[0], result[1]))


