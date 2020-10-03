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
    
    def move(self, move):
        if not move in self.get_available_moves():
            raise Exception("Move was not in available moves list.")

        current_player = self.current_player
        (row, col) = move
        cells_to_flip = []

        for direction in Directions:
            direction_cells_to_flip = self._would_flip_cells((row, col), direction)
            if direction_cells_to_flip is not None:
                for dir_cell_to_flip in direction_cells_to_flip:
                    cells_to_flip.append(dir_cell_to_flip)

        for cell_to_flip in cells_to_flip:
            (flip_cell_row, flip_cell_col) = cell_to_flip
            self.field[flip_cell_row][flip_cell_col] = self.current_player
        
        self.field[row][col] = current_player   

        self._available_moves = None
        self.current_player = self._get_opponent()

        # If player cannot make a move (get_available_moves length is zero)
        # Then we change player side and trying find availabale moves again
        # If even then there are no more moves - game is over
        while len(self.get_available_moves()) == 0:
            
            if self.current_player == current_player:
                self.current_player = Player.EMPTY
                break
            
            self.current_player = self._get_opponent()    

    def get_available_moves(self):
        if self._available_moves is not None:
            return self._available_moves
        
        moves = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                for direction in Directions:
                    cells_to_flip = self._would_flip_cells((row, col), direction)
                    if cells_to_flip is not None:
                        moves.append((row, col))
                        break
        
        self._available_moves = moves
        return moves

    def _would_flip_cells(self, cell, direction):
        flipped_cells = []
        (start_row, start_col) = cell
        
        row = start_row
        col = start_col
        
        if direction == Directions.UP:
            while row > 0:
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if row == start_row - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.DOWN:
            while row < len(self.field) - 1:
                row += 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if row == start_row + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.LEFT:
            while col > 0:
                col -= 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.RIGHT:
            while col < len(self.field[row]) - 1:
                col += 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.UPLEFT:
            while col > 0 and row > 0:
                col -= 1
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1 and row == start_row - 1:
                        return None
                    else:
                        return flipped_cells
        
        elif direction == Directions.UPRIGHT:
            while col < len(self.field[row]) - 1 and row > 0:
                col += 1
                row -= 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1 and row == start_row - 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.DOWNLEFT:
            while col > 0 and row < len(self.field) - 1:
                col -= 1
                row += 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col - 1 and row == start_row + 1:
                        return None
                    else:
                        return flipped_cells

        elif direction == Directions.DOWNRIGHT:
            while col < len(self.field[row]) - 1 and row < len(self.field) - 1:
                col += 1
                row += 1
                if self.field[row][col] == self._get_opponent():
                    flipped_cells.append((row, col))
                    continue
                elif self.field[row][col] == Player.EMPTY:
                    return None
                elif self.field[row][col] == self.current_player:
                    if col == start_col + 1 and row == start_row + 1:
                        return None
                    else:
                        return flipped_cells
