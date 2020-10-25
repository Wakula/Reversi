from model.constants import *
from model.field import Field

class Game:

    def __init__(self, black_hole=None):
        self.current_player = Player.BLACK
        self._field = Field(black_hole)
        self._available_moves = None
        self._prev_move_passed = False

    def get_winner(self):
        black_cells = self._field.get_players_points(Player.BLACK)
        white_cells = self._field.get_players_points(Player.WHITE)

        if black_cells < white_cells:
            return Player.BLACK
        elif white_cells < black_cells:
            return Player.WHITE
        else:
            return Player.EMPTY

    def move(self, move):
        if not move:
            self._available_moves = None
            if self._prev_move_passed:
                self.current_player = Player.EMPTY
                return

            self.current_player = self._field.get_opponent(self.current_player)
            self._prev_move_passed = True
            return

        self._prev_move_passed = False    
        current_player = self.current_player
        (row, col) = move
        cells_to_flip = []

        self._field.move(move, current_player)

        self._available_moves = None
        self.current_player = self._field.get_opponent(current_player)

    def get_field(self):
        return self._field

    def get_available_moves(self):
        if self._available_moves is None:
            self._available_moves = self._field.get_available_moves(self.current_player)

        return self._available_moves
