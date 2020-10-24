from model.constants import Player
from model.game import Game
from controller import players
from controller.input_mapper import InputMapper
from ui.field_printer import FieldPrinter


class GameController:
    INPUT_MAPPER = InputMapper

    OPPOSITE_PLAYER = {
        Player.BLACK: Player.WHITE,
        Player.WHITE: Player.BLACK
    }
    COLOR_NAMING_MAP = {
        'black': Player.BLACK,
        'white': Player.WHITE,
    }

    OMIKRON_BOT = players.OmikronBot
    KOROTENKO_BOT = players.KorotenkoBot

    def __init__(self, black_hole_input=None, omikron_color_input=None, include_ui=False):
        black_hole_coordinates = black_hole_input or input()
        color_input = omikron_color_input or input()
        omikron_bot_color = Player(self.COLOR_NAMING_MAP[color_input])
        korotenko_bot_color = Player(self.OPPOSITE_PLAYER[omikron_bot_color])
        self.game = Game(
            self.INPUT_MAPPER.get_coordinates(black_hole_coordinates)
        )
        self.players = {
            omikron_bot_color: self.OMIKRON_BOT(omikron_bot_color),
            korotenko_bot_color: self.KOROTENKO_BOT(korotenko_bot_color),
        }
        self.winner = None
        self.include_ui = include_ui

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
        game_field = self.game.get_field()
        player_move = self.players[self.game.current_player].select_move(game_field)
        self.game.move(player_move)

    def run_game(self):
        current_player = self.game.current_player
        while current_player != Player.EMPTY:
            if self.include_ui:
                self.print_field(current_player)
            self.move()
            current_player = self.game.current_player

        if self.include_ui:
            self.print_field(None, winner=self.game.get_winner().value)
