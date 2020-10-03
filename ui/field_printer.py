import time
from typing import Optional, List
import os


class FieldPrinter:
    WINNER_MESSAGES = {
        'black': 'Black player wins',
        'white': 'White player wins',
        'empty': 'Draw'
    }
    REMAIN_ON_SCREEN = 2

    def __init__(self, current_player: str, field: List[List[str]], winner: Optional[str], pass_move: bool):
        self.current_player = current_player
        self.field = field
        self.winner = winner
        self.pass_move = pass_move

    def print(self):
        os.system('clear')
        for row in self.field:
            print(row)
        if self.pass_move:
            print(f"{self.current_player} passes.")
        elif self.winner:
            print(self.WINNER_MESSAGES[self.winner])
        else:
            print(self.current_player)
        time.sleep(self.REMAIN_ON_SCREEN)
