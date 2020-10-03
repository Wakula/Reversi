from model.constants import *

class Game:

    def __init__(self):
        self.current_player = Player.BLACK
        self._side_length = 8

        self._init_field()


    def _init_field(self):
        self.field = [[Cell.EMPTY] * self._side_length for i in range(self._side_length)]

        half_length = self._side_length // 2

        self.field[half_length][half_length] = self.field[half_length + 1][half_length + 1] = Cell.WHITE
        self.field[half_length][half_length + 1] = self.field[half_length + 1][half_length] = Cell.BLACK

    def get_winner(self):
        black_cells = 0
        white_cells = 0

        for row in self.field:
            for cell in row:
                if cell == Cell.WHITE:
                    white_cells += 1
                elif cell == Cell.BLACK:
                    black_cells += 1
        
        if (black_cells > white_cells):
            return Player.BLACK
        elif (white_cells > black_cells):
            return Player.WHITE
        else:
            return Player.NONE

