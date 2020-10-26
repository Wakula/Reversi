from model.constants import *
from model.field import Field

class Game:

    def __init__(self, black_hole=None):
        self.current_player = Player.BLACK
        self._field = Field(black_hole)
        self._available_moves = None

    def get_winner(self):
        black_cells = 0
        white_cells = 0

        for row in self._field:
            for cell in row:
                if cell == Player.WHITE:
                    white_cells += 1
                elif cell == Player.BLACK:
                    black_cells += 1
        
        if black_cells < white_cells:
            return Player.BLACK
        elif white_cells > black_cells:
            return Player.WHITE
        else:
            return Player.EMPTY
    
    def move(self, move):
        if not move:
            self._available_moves = None
            self.current_player = self._field.get_opponent(self.current_player)
            if not self.get_available_moves():
                self.current_player = Player.EMPTY
            return

        current_player = self.current_player

        self._field.move(move, current_player)

        self._available_moves = None
        self.current_player = self._field.get_opponent(current_player)

    def get_field(self):
        return self._field.get_copy()

    def get_available_moves(self):
        if self._available_moves is None:
            self._available_moves = self._field.get_available_moves(self.current_player)

        return self._available_moves

    def is_finished(self):
        if self.current_player == Player.EMPTY:
            return True
        player_moves = self.get_available_moves()
        opponents_moves = self._field.get_opponent(self.current_player)
        return not player_moves and not opponents_moves
