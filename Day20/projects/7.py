# Music Player
import os, time

def play():
  print('🎵 MyPOD Music Player')
  print('1. Play')
  print('2. Exit')
  print('3. Menu')
  play= input('Do you want to play or exit?: ')
  if play == 'play':
      print('Playing soon...')
  elif play=='exit':
     print('Ending the music player')
  else:
     pass
print('Do you want to go back to the menu?: ')
menu = input('yes or no?:')
def menU():
  if menu == 'yes':
   return play()
  else:
   pass


time.sleep(0)
os.system('clear')        
play()