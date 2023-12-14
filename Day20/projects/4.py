# 2 player
from getpass import getpass as input
while True:
    score1 = 0
    score2 = 0
    player1 = input('Enter R,P,S:')
    player2 = input('Enter R,P,S:')
    if player1 == player2:
        score1 += 1
        score2 += 1
        print('Draw')
    elif player1 == 'R' and player2 == 'S':
        score1 += 1
        print('Player 1 wins')
    elif player1 == 'S' and player2 == 'R':
        score2 += 1
        print('Player 2 wins')
    elif player1 == 'P' and player2 == 'R':
        score1 += 1
        print('Player 1 wins')
    elif player1 == 'R' and player2 == 'P':
        score2 += 1
        print('Player 2 wins')
    elif player1 == 'S' and player2 == 'P':
       score1 += 1
       print('Player 1 wins')
    elif player1 == 'P' and player2 == 'S':
       score2 += 1
       print('Player 2 wins')
       break
    else:
        pass
        print('The winner is:','\n', 'player1 score: ',score1,'player2 score:',score2)