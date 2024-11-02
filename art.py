import random


class Board:
    def __init__(self):
        self.top = [' ', '', ' ', 'A', ' ', ' ', ' ', 'B', ' ', ' ', ' ', 'C', ' ',]
        self.first = ['1', ' ', '-', ' ', '|', ' ', '-', ' ', '|', ' ', '-', ' ']
        self.lines = ['---', '|', '---', '|', '---']
        self.second = ['2', ' ', '-', ' ', '|', ' ', '-', ' ', '|', ' ', '-', ' ']
        self.third = ['3', ' ', '-', ' ', '|', ' ', '-', ' ', '|', ' ', '-', ' ']
        self.filled_spots = []
        self.win_conditions = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3'], ['C1', 'C2', 'C3'], ['A1', 'B1', 'C1'],
                               ['A2', 'B2', 'C2'], ['A3', 'B3', 'C3'], ['A1', 'B2', 'C3'], ['C1', 'B2', 'A3']]
        self.player_wins = 0
        self.ai_wins = 0

    def move(self, input, player):
        moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        spaces = [(self.first, 2), (self.second, 2), (self.third, 2), (self.first, 6), (self.second, 6), (self.third, 6),
                  (self.first, 10), (self.second, 10), (self.third, 10)]
        mappings = dict(zip(moves, spaces))
        if input in mappings:
            if input not in self.filled_spots:
                row, index = mappings[input]
                row[index] = player
                self.filled_spots.append(input)
                self.print_board()
            else:
                print('Spot already taken, dear.')
        else:
            print('Not an option. Have you played this before?')
            self.print_board()

    def opp(self, opp):
        moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        opp_move = random.choice(moves)
        if opp_move not in self.filled_spots:
            self.move(input=opp_move, player=opp)
        else:
            self.opp(opp)

    def print_board(self):
        print(" " + ("").join(self.top))
        print(" " + ("").join(self.first))
        print("  " + ("").join(self.lines))
        print(" " + ("").join(self.second))
        print("  " + ("").join(self.lines))
        print(" " + ("").join(self.third))

    def win_check(self, player, opp):
        moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        spaces = [(self.first, 2), (self.second, 2), (self.third, 2), (self.first, 6), (self.second, 6),
                  (self.third, 6), (self.first, 10), (self.second, 10), (self.third, 10)]
        mappings = dict(zip(moves, spaces))
        for l in self.win_conditions:
            pcount = 0
            ocount = 0
            for i in l:
                data = mappings[i]
                row, index = data[0], data[1]
                if row[index] == player:
                    pcount += 1
                    if pcount == 3:
                        print(f'My fellow orthognian, you have won!! You got three {player}\'s in a row!')
                        return True
                elif row[index] == opp:
                    ocount += 1
                    if ocount == 3:
                        print(f'You neolithic troglodyte, you lost! Your opp got 3 {opp}\'s in a row!')
                        return True

"""
Mappings:
A1 = self.first[2]
A2 = self.second[2]
A3 = self.third[2]

B1 = self.first[6]
B2 = self.second[6]
B3 = self.third[6]

C1 = self.first[10]
C2 = self.second[10]
C3 = self.third[10]
------------------------
Win conditions:
[[A1, A2, A3],
[B1, B2, B3],
[C1, C2, C3],
[A1, B1, C1],
[A2, B2, C2],
[A3, B3, C3],
[A1, B2, C3],
[C1, B2, A3]]
"""
# if __name__ == '__main__':


