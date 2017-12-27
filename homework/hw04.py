"""
CS241 Homework 04
Written by Chad Macbeth
"""

from collections import deque

class Song:
   
   ### Initialize Song object 
   def __init__(self):
      self.title = ""
      self.artist = ""

   ### Prompt user to provide title and artist
   def prompt(self):
      self.title = input("Enter the title: ")
      self.artist = input("Enter the artist: ")

   ### dispaly song information
   def display(self):
      print ("{} by {}" .format(self.title, self.artist))

### Simulate a music playlist
def main():
   # Create a double eneded queue
   playlist = deque()
  
   # Loop until user selections option to quit 
   option = 0
   while (option != 4):
      print("Options:")
      print("1. Add a new song to the end of the playlist")
      print("2. Insert a new song to the beginning of the playlist")
      print("3. Play the next song")
      print("4. Quit")
      option = int(input("Enter selection: "))
      print()
      if (option == 1):
         # Create a song, populate it, and add to the end of the queue.
         song = Song()
         song.prompt()
         playlist.append(song)
         print()
      elif (option == 2):
         # Create a song, populate it, and add to the beginning of the queue
         song = Song()
         song.prompt()
         playlist.appendleft(song)
         print()
      elif (option == 3):
         # Display the playlist.  Display an error if its empty.
         if (len(playlist) == 0):
            print("The playlist is currently empty.") 
         else:
            song = playlist.popleft()
            print("Playing song:")
            song.display()
         print()
   print("Goodbye")

if __name__ == "__main__":
   main()
