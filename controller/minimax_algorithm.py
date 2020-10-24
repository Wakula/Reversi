from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class Result:
    value: float
    move: Optional[Tuple[int, int]] = None


INFINITY = float('inf')


class Node:
    def __init__(self, field, player, move):
        self.field = field
        self.player = player
        self.move = move
        self._children = None

    @property
    def is_terminal(self):
        next_player = self.field.get_opponent(self.player)
        return (not self.field.get_available_moves(self.player)) and (not self.field.get_available_moves(next_player))

    @property
    def value(self):
        return self.field.get_players_points(self.player)

    @property
    def children(self):
        if self._children:
            return self._children
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
        self._children = nodes
        return nodes


class MiniMaxReversi:
    NODE = Node
    DEPTH = 3

    @classmethod
    def _minimax(cls, node, alpha, beta, depth, maximizing_player) -> Result:
        if depth == 0 or node.is_terminal:
            return Result(value=node.value)
        if maximizing_player:
            result = Result(value=-INFINITY)
            for child in node.children:
                result = max(result, cls._minimax(child, alpha, beta, depth-1, False), key=lambda result: result.value)
                alpha = max(alpha, result.value)
                if beta <= alpha:
                    break
            if depth == cls.DEPTH - 1:
                result.move = node.move
            return result
        else:
            result = Result(value=INFINITY)
            for child in node.children:
                result = min(result, cls._minimax(child, alpha, beta, depth-1, True), key=lambda result: result.value)
                beta = min(beta, result.value)
                if beta <= alpha:
                    break
            if depth == cls.DEPTH - 1:
                result.move = node.move
            return result

    @classmethod
    def get_move(cls, game_field, player_color):
        initial_node = cls.NODE(game_field, player_color, None)
        result = cls._minimax(initial_node, -INFINITY, INFINITY, cls.DEPTH, True)

        return result.move
