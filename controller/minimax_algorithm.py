from dataclasses import dataclass
from typing import Optional, Tuple
import random


@dataclass
class Result:
    value: float
    move: Optional[Tuple[int, int]] = None


INFINITY = float('inf')

CORNERS = [
    (0, 0), (0, 7), (7, 0), (7, 7)
]


class Node:
    def __init__(self, field, player):
        self.field = field
        self.player = player
        self.opponent = self.field.get_opponent(self.player)
        self._available_moves = None

    @property
    def available_moves(self):
        if self._available_moves is not None:
            return self._available_moves
        self._available_moves = self._available_moves = self.field.get_available_moves(self.player)
        return self._available_moves

    @property
    def is_terminal(self):
        return (not self.field.get_available_moves(self.player)) and (not self.field.get_available_moves(self.opponent))

    @property
    def value(self):
        return self.field.get_players_points(self.player)

    @property
    def children(self):
        if not self.available_moves:
            return Node(self.field, self.opponent), None, lambda: ()
        for move in self.available_moves:
            flipped_cells = self.field.move(move, self.player)
            node = Node(self.field, self.opponent)
            yield node, move, lambda: self.field.undo_move(move, self.player, flipped_cells)


class MiniMaxReversi:
    NODE = Node
    DEPTH = 3

    @classmethod
    def _minimax(cls, node, alpha, beta, depth, maximizing_player) -> Result:
        if depth == 0 or node.is_terminal:
            return Result(value=node.value)
        if maximizing_player:
            result = Result(value=-INFINITY)
            for child, move, undo_move in node.children:
                minimax_result = cls._minimax(child, alpha, beta, depth-1, False)
                if move in CORNERS:
                    minimax_result.value = INFINITY
                alpha = max(alpha, result.value)
                undo_move()
                if minimax_result.value <= result.value:
                    result = minimax_result
                    result.move = move
                if beta <= alpha:
                    break
            return result
        else:
            result = Result(value=INFINITY)
            for child, move, undo_move in node.children:
                minimax_result = cls._minimax(child, alpha, beta, depth-1, True)
                if move in CORNERS:
                    minimax_result.value = -INFINITY
                beta = min(beta, result.value)
                undo_move()
                if minimax_result.value <= result.value:
                    result = minimax_result
                    result.move = move
                if beta <= alpha:
                    break
            return result

    @classmethod
    def get_move(cls, game_field, player_color):
        initial_node = cls.NODE(game_field, player_color)
        result = cls._minimax(initial_node, -INFINITY, INFINITY, cls.DEPTH, True)
        move = result.move
        if not move and initial_node.available_moves:
            move = random.choice(initial_node.available_moves)

        return move
