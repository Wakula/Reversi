from model.constants import *

class Game:

    def __init__(self):
        self.current_player = Player.BLACK
        self._side_length = 8

        self._init_field()


    def _init_field(self):
        self.field = [[Player.EMPTY] * self._side_length for i in range(self._side_length)]

        half_length = self._side_length // 2

        self.field[half_length][half_length] = self.field[half_length + 1][half_length + 1] = Player.WHITE
        self.field[half_length][half_length + 1] = self.field[half_length + 1][half_length] = Player.BLACK

    def get_winner(self):
        black_cells = 0
        white_cells = 0

        for row in self.field:
            for cell in row:
                if cell == Player.WHITE:
                    white_cells += 1
                elif cell == Player.BLACK:
                    black_cells += 1
        
        if black_cells > white_cells:
            return Player.BLACK
        elif white_cells > black_cells:
            return Player.WHITE
        else:
            return Player.EMPTY
    
    def get_available_moves(self):
        moves = []
        for row in range(len(self.field)):
            for cell in range(len(row)):
                pass

    
    def would_flip_to(self, cell, diretion):
        pass