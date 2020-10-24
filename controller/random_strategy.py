import random


class RandomStrategy:
    @classmethod
    def get_move(cls, game_field, player_color):
        available_moves = game_field.get_available_moves(player_color)
        if not available_moves:
            return
        return available_moves[random.randint(0, len(available_moves) - 1)]
