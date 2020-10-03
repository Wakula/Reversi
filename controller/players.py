import random
from typing import Tuple, List


class AbstractPlayer:
    def select_move(self, available_moves: List[Tuple[int, int]]) -> Tuple[int, int]:
        pass


class AiPlayer(AbstractPlayer):
    def select_move(self, available_moves: List[Tuple[int, int]]) -> Tuple[int, int]:
        return available_moves[random.randint(0, len(available_moves) - 1)]


class HumanPlayer(AbstractPlayer):
    def select_move(self, available_moves: List[Tuple[int, int]]) -> Tuple[int, int]:
        print("Dear Player Input x, y coordinates to move please.")
        invalid_input = True
        while invalid_input:
            print(f"Here are your available options. {available_moves}")
            print('x=', end='')
            x = int(input())
            print('y=', end='')
            y = int(input())
            if (x, y) not in available_moves:
                print(f"({x}, {y}) is not one of available moves. {available_moves}")
            else:
                invalid_input = False

        return x, y
