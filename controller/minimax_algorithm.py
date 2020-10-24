from collections import namedtuple
import time

MoveValue = namedtuple('MoveValue', ['move', 'value'])


class Node:
    def __init__(self, field, player, move):
        self.field = field
        self.player = player
        self.move = move

    @property
    def is_terminal(self):
        next_player = self.field.get_opponent(self.player)
        return (not self.field.get_available_moves(self.player)) and (not self.field.get_available_moves(next_player))

    @property
    def value(self):
        return self.field.get_players_points(self.player)

    @property
    def children(self):
        nodes = []
        next_player = self.field.get_opponent(self.player)
        available_moves = self.field.get_available_moves(self.player)
        if not available_moves:
            current_field = self.field.get_copy()
            return [Node(current_field, next_player, None)]
        for move in available_moves:
            current_field = self.field.get_copy()
            current_field.move(move, self.player)
            node = Node(current_field, next_player, move)
            nodes.append(node)
        return nodes


class MiniMaxReversi:
    NODE = Node

    def __init__(self, maximizing_player, depth):
        self.maximizing_player = maximizing_player
        self.depth = depth

    def _minimax(self, node, depth, maximizing_player):
        if depth == 0 or node.is_terminal:
            return node.value
        if maximizing_player:
            value = -float('inf')
            for child in node.children:
                value = max(value, self._minimax(child, depth-1, False))
            return value
        else:
            value = float('inf')
            for child in node.children:
                value = min(value, self._minimax(child, depth-1, True))
            return value

    def get_move(self, game_field, player_color):
        move_values = []
        available_moves = game_field.get_available_moves(player_color)

        if not available_moves:
            return None
        for move in available_moves:
            node = self.NODE(game_field, player_color, move)
            move_value = MoveValue(
                move=move,
                value=self._minimax(node, self.depth, self.maximizing_player)
            )
            move_values.append(move_value)

        return max(move_values, key=lambda move_value: move_value.value).move
