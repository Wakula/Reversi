from controller.game_controller import GameController
from controller.players import TestBot
from model.constants import Player
import random


class TestController(GameController):
    KOROTENKO_BOT = TestBot


class TestReversi:
    GAME_CONTROLLER = TestController
    COLOR = ['black', 'white']
    Y_MAPPINGS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    INVALID_BLACK_HOLE = ['D4', 'E4', 'D5', 'E5', '']
    STALEMATE = 'Stalemate'
    OMIKRON_BOT = 'Omikron Bot'
    RANDOM_BOT = 'Random Bot'

    def __init__(self, *, tests_amount, include_ui):
        self.winners = {
            self.STALEMATE: 0,
            self.OMIKRON_BOT: 0,
            self.RANDOM_BOT: 0,
        }
        self.tests_amount = tests_amount
        self.include_ui = include_ui

    def test(self):
        for i in range(self.tests_amount):
            omikron_color = random.choice(self.COLOR)
            print(f'------|OMIKRON BOT COLOR = {omikron_color}|------')
            black_hole = ''
            while black_hole in self.INVALID_BLACK_HOLE:
                black_hole = f'{random.choice(self.Y_MAPPINGS)}{random.randint(1, 8)}'
            game = self.GAME_CONTROLLER(
                omikron_color_input=omikron_color,
                black_hole_input=black_hole,
                include_ui=self.include_ui
            )
            game.run_game()
            winner = game.game.get_winner()
            print('BLACK', game.game._field.get_players_points(Player.BLACK))
            print('WHITE', game.game._field.get_players_points(Player.WHITE))
            if winner == Player.EMPTY:
                self.winners[self.STALEMATE] += 1
                continue
            if (omikron_color == 'black' and winner == Player.BLACK) or (omikron_color == 'white' and winner == Player.WHITE):
                self.winners[self.OMIKRON_BOT] += 1
                continue
            self.winners[self.RANDOM_BOT] += 1
        print(self.winners)


TestReversi(
    tests_amount=100,
    include_ui=True,
).test()
