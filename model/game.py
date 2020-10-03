from model.constants import *

class Game:

    def __init__(self):
        self.current_player = Player.BLACK
        self._side_length = 8
        self._available_moves = None
        self._init_field()


    def _init_field(self):
        self.field = [[Player.EMPTY] * self._side_length for i in range(self._side_length)]

        half_length = self._side_length // 2

        self.field[half_length - 1][half_length - 1] = self.field[half_length][half_length] = Player.BLACK
        self.field[half_length - 1][half_length] = self.field[half_length][half_length - 1] = Player.WHITE

    def _get_opponent(self):
        if self.current_player == Player.BLACK:
            return Player.WHITE
        elif self.current_player == Player.WHITE:
            return Player.BLACK
        else:
            return None   

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
        if self._available_moves is not None:
            return self._available_moves
        
        moves = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                for direction in Directions:
                    flip_to_cell = self._would_flip_to((row, col), direction)
                    if flip_to_cell is not None:
                        moves.append((row, col))
                        break
        
        self._available_moves = moves
        return moves

    def _would_flip_to(self, cell, direction):
        (start_row, start_col) = cell
        
        row = start_row
        col = start_col
        
        if direction == Directions.UP:
            while row > 0:
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if row == start_row - 1:
                        return None
                    else:
                        return (row, col)
        
        elif direction == Directions.DOWN:
            while row < len(self.field) - 1:
                row += 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if row == start_row + 1:
                        return None
                    else:
                        return (row, col)

        elif direction == Directions.LEFT:
            while col > 0:
                col -= 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1:
                        return None
                    else:
                        return (row, col)
        
        elif direction == Directions.RIGHT:
            while col < len(self.field[row]) - 1:
                col += 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1:
                        return None
                    else:
                        return (row, col)

        elif direction == Directions.UPLEFT:
            while col > 0 and row > 0:
                col -= 1
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1 and row == start_row - 1:
                        return None
                    else:
                        return (row, col)
        
        elif direction == Directions.UPRIGHT:
            while col < len(self.field[row]) - 1 and row > 0:
                col += 1
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1 and row == start_row - 1:
                        return None
                    else:
                        return (row, col)

        elif direction == Directions.DOWNLEFT:
            while col > 0 and row < len(self.field) - 1:
                col -= 1
                row += 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1 and row == start_row + 1:
                        return None
                    else:
                        return (row, col)

        elif direction == Directions.DOWNRIGHT:
            while col < len(self.field[row]) - 1 and row < len(self.field) - 1:
                col += 1
                row += 1
                if self.field[row][col] == self._get_opponent():
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1 and row == start_row + 1:
                        return None
                    else:
                        return (row, col)

