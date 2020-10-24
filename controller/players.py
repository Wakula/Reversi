import random
from typing import Tuple, Optional
from controller.input_mapper import InputMapper
from model.field import Field
from model.constants import Player
from controller.minimax_algorithm import MiniMaxReversi


class AbstractPlayer:
    INPUT_MAPPER = InputMapper
    
    def __init__(self, player_color: Player):
        self.player_color = player_color

    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        pass


class OmikronBot(AbstractPlayer):
    AI_STRATEGY = MiniMaxReversi

    def __init__(self, player_color: Player):
        super().__init__(player_color)
        self.ai_strategy = self.AI_STRATEGY(
            maximizing_player=False,
            depth=2
        )

    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        selected_move = self.ai_strategy.get_move(game_field, self.player_color)
        if not selected_move:
            print('pass')
            return
        print(self.INPUT_MAPPER.get_mapping(selected_move))
        return selected_move


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
