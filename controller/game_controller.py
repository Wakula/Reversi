from model.constants import Player
from model.game import Game
from controller import constants
from controller import players
from controller.input_mapper import InputMapper
from ui.field_printer import FieldPrinter


class GameController:
    INPUT_MAPPER = InputMapper

    OPPONENT_TYPES = {
        constants.KOROTENKO_BOT: players.KorotenkoBot,
        constants.OMIKRON_BOT: players.OmikronBot,
    }
    OPPOSITE_PLAYER = {
        Player.BLACK: Player.WHITE,
        Player.WHITE: Player.BLACK
    }
    COLOR_NAMING_MAP = {
        'black': Player.BLACK,
        'white': Player.WHITE,
    }

    def __init__(self):
        black_hole_coordinates = input()
        omikron_bot_color = Player(self.COLOR_NAMING_MAP[input()])
        korotenko_bot_color = Player(self.OPPOSITE_PLAYER[omikron_bot_color])
        self.game = Game(
            self.INPUT_MAPPER.get_coordinates(black_hole_coordinates)
        )
        self.players = {
            omikron_bot_color: players.OmikronBot(),
            korotenko_bot_color: players.KorotenkoBot(),
        }
        self.winner = None

    def print_field(self, current_player, *, winner=None, pass_move=False):
        field = [[cell.value for cell in row] for row in self.game.get_field().field]
        field_printer = FieldPrinter(
            current_player.value if current_player else None,
            field,
            winner,
            pass_move,
            self.game.get_available_moves())
        field_printer.print()

    def move(self):
        available_moves = self.game.get_available_moves()
        player_move = self.players[self.game.current_player].select_move(available_moves)
        self.game.move(player_move)

    def run_game(self):
        current_player = self.game.current_player
        while current_player != Player.EMPTY:
            # self.print_field(current_player)
            self.move()
            current_player = self.game.current_player

        # self.print_field(None, winner=self.game.get_winner().value)

    def end_game(self):
        end_map = {
            'yes': False,
            'no': True
        }

        while True:
            print('Restart game? yes/no')
            end = input()
            if end not in end_map:
                print(f'{end} not in (yes, no)')
            else:
                return end_map[end]
