from typing import Optional, List


class FieldPrinter:
    Y_MAPPING_TO_COORDINATES = {
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'F',
        6: 'G',
        7: 'H',
    }

    WINNER_MESSAGES = {
        'B': 'Black player wins',
        'W': 'White player wins',
        ' ': 'Draw'
    }
    PLAYER_OUTPUT = {
        'W': 'White player turn',
        'B': 'Black player turn',
    }

    def __init__(
            self,
            current_player: str,
            field: List[List[str]],
            winner: Optional[str],
            pass_move: bool,
            available_moves,
    ):
        self.current_player = current_player
        self.field = field
        self.winner = winner
        self.pass_move = pass_move
        self.available_moves = available_moves

    def prepare_output(self):
        prepared_field = []
        coordinates = [self.Y_MAPPING_TO_COORDINATES[i] for i in range(len(self.field))]
        prepared_field.append(['+'] + coordinates)
        for x in range(len(self.field)):
            row = [str(x+1)]
            for y in range(len(self.field[x])):
                if (x, y) in self.available_moves:
                    row.append('*')
                else:
                    row.append(self.field[x][y])
            prepared_field.append(row)
        return prepared_field

    def print(self):
        for row in self.prepare_output():
            print(row)
        if self.pass_move:
            print(f"{self.PLAYER_OUTPUT[self.current_player]} passes.")
        elif self.winner:
            print(self.WINNER_MESSAGES[self.winner])
        else:
            print(f"{self.PLAYER_OUTPUT[self.current_player]}")
