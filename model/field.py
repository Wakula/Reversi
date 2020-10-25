from model.cell_flipper import CellFlipper
from model.constants import *
import copy


class Field:
    FLIP_CELLS = {
        Directions.UP: lambda flipper: flipper.flip_up(),
        Directions.DOWN: lambda flipper: flipper.flip_down(),
        Directions.LEFT: lambda flipper: flipper.flip_left(),
        Directions.RIGHT: lambda flipper: flipper.flip_right(),
        Directions.UPLEFT: lambda flipper: flipper.flip_up_left(),
        Directions.UPRIGHT: lambda flipper: flipper.flip_up_right(),
        Directions.DOWNLEFT: lambda flipper: flipper.flip_down_left(),
        Directions.DOWNRIGHT: lambda flipper: flipper.flip_down_right(),
    }

    CELL_FLIPPER = CellFlipper

    def __init__(self, black_hole=None):
        self._side_length = 8
        self.field = [[Player.EMPTY] * self._side_length for i in range(self._side_length)]

        half_length = self._side_length // 2

        self.field[half_length - 1][half_length - 1] = self.field[half_length][half_length] = Player.WHITE
        self.field[half_length - 1][half_length] = self.field[half_length][half_length - 1] = Player.BLACK

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
        moves = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.field[row][col] == Player.EMPTY:
                    for direction in Directions:
                        cells_to_flip = self._would_flip_cells((row, col), direction, player)
                        if cells_to_flip is not None:
                            moves.append((row, col))
                            break
        return moves

    def get_players_points(self, player):
        points = 0

        for row in self.field:
            for cell in row:
                if cell == player:
                    points += 1
        
        return points

    def move(self, move, player) -> list:
        if not move in self.get_available_moves(player):
            raise Exception("Move was not in available moves list.")

        (row, col) = move
        cells_to_flip = []

        for direction in Directions:
            direction_cells_to_flip = self._would_flip_cells((row, col), direction, player)
            if direction_cells_to_flip is not None:
                for dir_cell_to_flip in direction_cells_to_flip:
                    cells_to_flip.append(dir_cell_to_flip)

        for cell_to_flip in cells_to_flip:
            (flip_cell_row, flip_cell_col) = cell_to_flip
            self.field[flip_cell_row][flip_cell_col] = player
        
        self.field[row][col] = player

        return cells_to_flip

    def get_copy(self):
        new_field = Field()
        new_field.field = copy.deepcopy(self.field)
        return new_field

    def _would_flip_cells(self, cell, direction, player):
        flipped_cells = []
        (start_row, start_col) = cell
        
        row = start_row
        col = start_col

        opponent = self.get_opponent(player)
        flipper = self.CELL_FLIPPER(
            row=row,
            col=col,
            opponent=opponent,
            flipped_cells=flipped_cells,
            player=player,
            start_row=start_row,
            start_col=start_col,
            field=self.field
        )
        return self.FLIP_CELLS[direction](flipper)

    def undo_move(self, move, player, cells_to_flip):
        opponent = self.get_opponent(player)
        row, col = move

        for cell_to_flip in cells_to_flip:
            (flip_cell_row, flip_cell_col) = cell_to_flip
            self.field[flip_cell_row][flip_cell_col] = opponent

        self.field[row][col] = Player.EMPTY
