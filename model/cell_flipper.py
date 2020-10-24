from model.constants import *


class CellFlipper:
    def __init__(self, *, row, col, opponent, flipped_cells, player, start_row, start_col, field):
        self.row = row
        self.col = col
        self.opponent = opponent
        self.flipped_cells = flipped_cells
        self.player = player
        self.start_row = start_row
        self.field = field
        self.start_col = start_col

    def flip_down(self):
        while self.row > 0:
            self.row -= 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.row == self.start_row - 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_up(self):
        while self.row > 0:
            self.row -= 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.row == self.start_row - 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_left(self):
        while self.col > 0:
            self.col -= 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col - 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_right(self):
        while self.col < len(self.field[self.row]) - 1:
            self.col += 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col + 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_up_left(self):
        while self.col > 0 and self.row > 0:
            self.col -= 1
            self.row -= 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col - 1 and self.row == self.start_row - 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_up_right(self):
        while self.col < len(self.field[self.row]) - 1 and self.row > 0:
            self.col += 1
            self.row -= 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col + 1 and self.row == self.start_row - 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_down_left(self):
        while self.col > 0 and self.row < len(self.field) - 1:
            self.col -= 1
            self.row += 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col - 1 and self.row == self.start_row + 1:
                    return None
                else:
                    return self.flipped_cells

    def flip_down_right(self):
        while self.col < len(self.field[self.row]) - 1 and self.row < len(self.field) - 1:
            self.col += 1
            self.row += 1
            if self.field[self.row][self.col] == self.opponent:
                self.flipped_cells.append((self.row, self.col))
                continue
            elif self.field[self.row][self.col] == Player.EMPTY or self.field[self.row][self.col] == Player.HOLE:
                return None
            elif self.field[self.row][self.col] == self.player:
                if self.col == self.start_col + 1 and self.row == self.start_row + 1:
                    return None
                else:
                    return self.flipped_cells
