import random
from typing import Tuple, List, Optional
from controller.input_mapper import InputMapper


class AbstractPlayer:
    INPUT_MAPPER = InputMapper

    def select_move(self, available_moves: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
        pass


class OmikronBot(AbstractPlayer):
    def select_move(self, available_moves: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
        if not available_moves:
            print('pass')
            return
        selected_move = available_moves[random.randint(0, len(available_moves) - 1)]
        move = selected_move
        print(self.INPUT_MAPPER.get_mapping(move))
        return move


class KorotenkoBot(AbstractPlayer):
    def select_move(self, available_moves: List[Tuple[int, int]]) -> Optional[Tuple[int, int]]:
        if not available_moves:
            return
        # print("Dear Player Input x, y coordinates to move please.")
        invalid_input = True
        while invalid_input:
            x, y = self.INPUT_MAPPER.get_coordinates(input())
            if (x, y) not in available_moves:
                # print(f"({x}, {y}) is not one of available moves. {available_moves}")
                pass
            else:
                invalid_input = False

        return x, y
