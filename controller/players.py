import random
from typing import Tuple, List, Optional
from controller.input_mapper import InputMapper
from model.field import Field
from model.constants import Player


class AbstractPlayer:
    INPUT_MAPPER = InputMapper
    
    def __init__(self, player_color: Player):
        self.player_color = player_color

    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        pass


class OmikronBot(AbstractPlayer):
    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        available_moves = game_field.get_available_moves(self.player_color)
        if not available_moves:
            print('pass')
            return
        selected_move = available_moves[random.randint(0, len(available_moves) - 1)]
        move = selected_move
        print(self.INPUT_MAPPER.get_mapping(move))
        return move


class KorotenkoBot(AbstractPlayer):
    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        available_moves = game_field.get_available_moves(self.player_color)
        if not available_moves:
            return
        # print("Dear Player Input x, y coordinates to move please.")
        invalid_input = True
        while invalid_input:
            try:
                x, y = self.INPUT_MAPPER.get_coordinates(input())
            except ValueError:
                return None
            if (x, y) not in available_moves:
                # print(f"({x}, {y}) is not one of available moves. {available_moves}")
                pass
            else:
                invalid_input = False

        return x, y
