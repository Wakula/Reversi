from model.constants import *
import copy

class Field:
    
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

    def move(self, move, player):
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
        
        if direction == Directions.UP:
            while row > 0:
                row -= 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if row == start_row - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.DOWN:
            while row < len(self.field) - 1:
                row += 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if row == start_row + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.LEFT:
            while col > 0:
                col -= 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.RIGHT:
            while col < len(self.field[row]) - 1:
                col += 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.UPLEFT:
            while col > 0 and row > 0:
                col -= 1
                row -= 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col - 1 and row == start_row - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.UPRIGHT:
            while col < len(self.field[row]) - 1 and row > 0:
                col += 1
                row -= 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col + 1 and row == start_row - 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.DOWNLEFT:
            while col > 0 and row < len(self.field) - 1:
                col -= 1
                row += 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col - 1 and row == start_row + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.DOWNRIGHT:
            while col < len(self.field[row]) - 1 and row < len(self.field) - 1:
                col += 1
                row += 1
                if self.field[row][col] == opponent:
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY or self.field[row][col] == Player.HOLE:
                    return None
                elif self.field[row][col] == player:
                    if col == start_col + 1 and row == start_row + 1:
                        return None
                    else:
                        return flipped_cells