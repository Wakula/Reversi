import random
from typing import Tuple, Optional
from controller.input_mapper import InputMapper
from model.field import Field
from model.constants import Player
from controller.minimax_algorithm import MiniMaxReversi
from controller.random_strategy import RandomStrategy


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

    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        selected_move = self.AI_STRATEGY.get_move(game_field, self.player_color)
        print(self.INPUT_MAPPER.get_mapping(selected_move))
        return selected_move


class KorotenkoBot(AbstractPlayer):
    def select_move(self, game_field: Field) -> Optional[Tuple[int, int]]:
        return self.INPUT_MAPPER.get_coordinates(input())


class TestBot(OmikronBot):
    AI_STRATEGY = RandomStrategy
