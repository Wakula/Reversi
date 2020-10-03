import time
from typing import Optional, List, Tuple


class FieldPrinter:
    WINNER_MESSAGES = {
        'black': 'Black player wins',
        'white': 'White player wins',
        'empty': 'Draw'
    }
    PLAYER_OUTPUT = {
        'W': 'White player',
        'B': 'Black player',
    }

    def __init__(
            self,
            current_player: str,
            field: List[List[str]],
            winner: Optional[str],
            move: Optional[Tuple[str, str]]
    ):
        self.current_player = current_player
        self.field = field
        self.winner = winner
        self.move = move

    def print(self):
        for row in self.field:
            print(row)
        if not self.move and not self.winner:
            print(f"{self.current_player} passes.")
        elif self.winner:
            print(self.WINNER_MESSAGES[self.winner])
        else:
            print(self.current_player)
