import random
import sys

class GameManager():

    def __init__(self):
        print('------------------------------')
        print('Welcome to RPS!')
        print('------------------------------')
        print('**You can  exit anytime by typing exit.**')

        self.moves = {'rock': '⬛️', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves = list(self.moves.keys())
        self.ties = 0
        self.player_wins = 0
        self.ai_wins = 0
        self.total_games = 0

    def game_play(self):
        print('------------------------------')
        user_move = input('Your turn: Rock, Paper or Scissors? -> ').lower()
        opponent_move = self.ai_move()
        
        if user_move == 'exit':
            print('Thanks for playing.')
            sys.exit()
        elif user_move not in self.valid_moves:
            print('Invalid move!')
            return self.game_play()
        
        self.display_moves(user_move, opponent_move)
        self.check_moves(user_move, opponent_move)

    def ai_move(self):
        #Can be more sophisticated algorithms!
        return(random.choice(self.valid_moves))

    def display_moves(self, user_move, opponent_move):
        print('------------------------------')
        print(f'You: {self.moves[user_move]}')
        print(f'AI: {self.moves[opponent_move]}')
        print('------------------------------')

    def check_moves(self, user_move, opponent_move):
        if user_move == opponent_move:
            print('It is a tie!')
            self.statistics('0')
        elif user_move == 'rock' and opponent_move == 'scissors':
            print('You Win!')
            self.statistics('1')
        elif user_move == 'scissors' and opponent_move == 'paper':
            print('You Win!')
            self.statistics('1')
        elif user_move == 'paper' and opponent_move == 'rock':
            print('You Win!')
            self.statistics('1')
        else:
            print('AI wins...')
            self.statistics('2')

    def statistics(self, result):
        if result == '0':
            self.ties += 1
        elif result == '1':
            self.player_wins += 1
        else:
            self.ai_wins += 1
        
        self.total_games = self.ties + self.player_wins + self.ai_wins
        player_win_ratio = self.player_wins / self.total_games
        print(f'Total games: {self.total_games}')
        print(f'You have won: {self.player_wins}, "{round(player_win_ratio * 100, 2)}%"')
        
if __name__ == '__main__':
    rps = GameManager()
    while True:
        rps.game_play()