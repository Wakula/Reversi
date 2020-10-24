from model.constants import Player
from model.game import Game
from controller import constants
from controller import players
from ui.field_printer import FieldPrinter


class GameController:
    OPPONENT_TYPES = {
        constants.HUMAN_PLAYER: players.HumanPlayer,
        constants.AI_PLAYER: players.AiPlayer,
    }
    OPPOSITE_PLAYER = {
        Player.BLACK: Player.WHITE,
        Player.WHITE: Player.BLACK
    }

    def __init__(self):
        self.game = Game()
        self.players = {}
        self.winner = None

    def prepare_game(self):
        print('Select Player to play against. Other player or AI.')
        invalid_input = True
        while invalid_input:
            print(f'Choices are {constants.PLAYER_TYPES}')
            print('opponent=', end='')
            opponent = str(input())
            if opponent not in constants.PLAYER_TYPES:
                print(f"{opponent} is invalid input.")
            else:
                invalid_input = False
        self.players[Player.BLACK] = players.HumanPlayer()
        self.players[Player.WHITE] = self.OPPONENT_TYPES[opponent]()

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
        previous_player = Player.EMPTY
        while current_player != Player.EMPTY:
            self.print_field(current_player)
            self.move()
            previous_player = current_player
            current_player = self.game.current_player
            if previous_player == current_player:
                self.print_field(self.OPPOSITE_PLAYER[current_player], pass_move=True)

        self.print_field(None, winner=self.game.get_winner().value)

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
