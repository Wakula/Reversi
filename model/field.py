from model.constants import *
from model.cache import Cache
import copy


class Field:
    
    DIRECTION_MAPPINGS = {
        Directions.DOWN: lambda row, col: (row+1, col),
        Directions.UP: lambda row, col: (row-1, col),
        Directions.LEFT: lambda row, col: (row, col-1),
        Directions.RIGHT: lambda row, col: (row, col+1),
        Directions.DOWNLEFT: lambda row, col: (row+1, col-1),
        Directions.DOWNRIGHT: lambda row, col: (row+1, col+1),
        Directions.UPLEFT: lambda row, col: (row-1, col-1),
        Directions.UPRIGHT: lambda row, col: (row-1, col+1)
    }

    def __init__(self, black_hole=None):
        self._side_length = 8
        self._cache = Cache.get_instance()
        self.field = [[Player.EMPTY] * self._side_length for i in range(self._side_length)]

        half_length = self._side_length // 2

        self.field[half_length - 1][half_length - 1] = self.field[half_length][half_length] = Player.WHITE
        self.field[half_length - 1][half_length] = self.field[half_length][half_length - 1] = Player.BLACK
        self.black_hole = black_hole

        if black_hole is not None:
            (row, col) = black_hole
            self.field[row][col] = Player.HOLE

    def get_opponent(self, player):
        if player == Player.BLACK:
            return Player.WHITE
        elif player == Player.WHITE:
            return Player.BLACK
        else:
            return None   

    def get_available_moves(self, player):
        cached_moves = self._cache.try_get_moves(self.field, player)
        if cached_moves is not None:
            return cached_moves

        moves = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.field[row][col] == Player.EMPTY:
                    for direction in Directions:
                        cells_to_flip = self._get_flipped_cells((row, col), direction, player)
                        if cells_to_flip:
                            moves.append((row, col))
                            break

        self._cache.save_state(self.field, player, moves)
        return moves

    def get_players_points(self, player):
        points = 0

        for row in self.field:
            for cell in row:
                if cell == player:
                    points += 1
        
        return points

    def move(self, move, player) -> list:
        if move not in self.get_available_moves(player):
            raise Exception("Move was not in available moves list.")

        (row, col) = move
        cells_to_flip = []

        for direction in Directions:
            cells_to_flip += self._get_flipped_cells((row, col), direction, player)

        if cells_to_flip:
            for cell_to_flip in cells_to_flip:
                (flip_cell_row, flip_cell_col) = cell_to_flip
                self.field[flip_cell_row][flip_cell_col] = player
        
        self.field[row][col] = player

        return cells_to_flip
    
    def undo_move(self, move, player, cells_to_flip):
        opponent = self.get_opponent(player)
        row, col = move

        for cell_to_flip in cells_to_flip:
            (flip_cell_row, flip_cell_col) = cell_to_flip
            self.field[flip_cell_row][flip_cell_col] = opponent

        self.field[row][col] = Player.EMPTY

    def get_copy(self):
        new_field = Field()
        new_field.field = copy.deepcopy(self.field)
        return new_field

    def _get_flipped_cells(self, start_cell, direction, player):
        flipped_cells = []
        (start_row, start_col) = start_cell
        opponent = self.get_opponent(player)

        apply_direction = self.DIRECTION_MAPPINGS[direction]
        row, col = apply_direction(start_row, start_col)
        
        while not self._is_out_of_field(row, col):
            if self.field[row][col] == opponent:
                flipped_cells.append((row, col))
                row, col = apply_direction(row, col)
                continue
            elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                return []
            elif self.field[row][col] == player:
                if abs(row - start_row) == 1 or abs(col - start_col) == 1:
                    return []
                return flipped_cells
                
        return []
    
    def _is_out_of_field(self, row, col):
        field_row_length = len(self.field)
        field_col_length = len(self.field[0])

        return row < 0 or col < 0 or row > field_col_length - 1 or col > field_row_length - 1
