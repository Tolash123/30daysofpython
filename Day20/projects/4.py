# 2 player
from getpass import getpass as input
player1 = input('Enter R,P,S:')
player2 = input('Enter R,P,S:')
if player1 == player2:
    print('Draw')
elif player1 == 'R' and player2 == 'S':
    print('Player 1 wins')
elif player1 == 'S' and player2 == 'R':
    print('Player 2 wins')
elif player1 == 'P' and player2 == 'R':
    print('Player 1 wins')
elif player1 == 'R' and player2 == 'P':
    print('Player 2 wins')
elif player1 == 'S' and player2 == 'P':
    print('Player 1 wins')
elif player1 == 'P' and player2 == 'S':
    print('Player 2 wins')