"""
CS241 Team Activity 1 - Stretch 
Written by Chad Macbeth
"""

### compareDna will return the number of matches and the percent match 
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
   return (match, match_percent)

dna_seq = input("Please enter your DNA sequence: ")

# Get the number of friends
num_friends_str = input("How many friends: ")
num_friends = int(num_friends_str)

# Get the friend names and store them in a list
friend_name_list = []
for i in range(num_friends):  # Loop 0 to num_friends-1
   friend_name = input("Please enter your friend #{} name: " .format(i+1))
   friend_name_list.append(friend_name)  # Add to the end of the list

# Get the friend DNA and store them in a list
friend_dna_seq_list = []
for i in range(num_friends):
   friend_dna_seq = input("Enter the DNA sequence for {}: " .format(friend_name_list[i]))
   friend_dna_seq_list.append(friend_dna_seq)  # Add to the end of the list

# Display match results
for i in range(num_friends):
   (match, match_percent) = compare_dna(dna_seq, friend_dna_seq_list[i])
   print("You and your friend {} had {} matches for {}%" .format(friend_name_list[i], match, match_percent))


