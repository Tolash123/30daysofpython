class Game:
    score1 = 0
    score2 = 0
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        Game.score1 += 1
        Game.score2 += 1
    def score(self):
        print('player1 score is %d' %Game.score1)
        print('player2 score is %d'%Game.score2)

    def game(self):
        while True:
            self.player1 = input('Enter R,P,S: ')
            self.player2 = input('Enter R,P,S: ')
            if self.player1 == self.player2:
                print('Draw')
                print('Player1: {}'.format(Game.score1))
                print('player2: {}'.format(Game.score2))
            elif self.player1 == 'R' and self.player2 == 'S':
                print('The winner is {}'.format(self.player1))
                print('Player1: {}'.format(Game.score1))
                print('player2: {}'.format(Game.score2-1))
            elif self.player1 == 'S' and self.player2 == 'R':
                print('The winner is {}'.format(self.player2))
                print('Player1: {}'.format(Game.score1-1))
                print('player2: {}'.format(Game.score2))
            elif self.player1 == 'R' and self.player2 == 'p':
                print('The winner is {}'.format(self.player1))
                print('Player1: {}'.format(Game.score1))
                print('player2: {}'.format(Game.score2-1))
            elif self.player1 == 'p' and self.player2 == 'R':
                print('The winner is {}'.format(self.player2))
                print('Player1: {}'.format(Game.score1-1))
                print('player2: {}'.format(Game.score2))
            elif self.player1 == 'R' and self.player2 == 'S':
                print('The winner is {}'.format(self.player1))
                print('Player1: {}'.format(Game.score1))
                print('player2: {}'.format(Game.score2-1))
                break
            else:
                pass
                print('This is the end!')
                exit()
d = Game('Idris','Hafeez')
e = Game('Hafeez','Idris')
d.game()
e.game()
print('Player1: {}'.format(Game.score1))
print('player2: {}'.format(Game.score2))