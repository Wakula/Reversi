from dataclasses import dataclass
from typing import Optional, Tuple
from model.constants import Player
import math
import random


@dataclass
class Result:
    value: float
    move: Optional[Tuple[int, int]] = None


INFINITY = float('inf')
"""
HEAT_MAP = [
    [0.0, 8,  0.2, 0.5, 0.5, 0.2,  8,  0.0],
    [8,  1.2,    0.25,   5,   5,   0.25, 1.2,   8],
    [0.2, 0.25,  0.2,   1,   1, 0.2,  0.25,  0.2],
    [0.5, 5,    1,   1,   1,   1,  5,  0.5],
    [0.5, 5,    1,   1,   1,   1,  5,  0.5],
    [0.2, 0.25,  0.2,   1,   1, 0.2,  0.25,  0.2],
    [8,  1.2,    0.25,   5,   5,   0.25, 1.2,   8],
    [0.0, 8,  0.2, 0.5, 0.5, 0.2,  8,  0.0]
]
"""

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
        #return (self.field.get_players_points(self.field.get_opponent(self.player)) + 1) / (self.field.get_players_points(self.player) + 1)

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
    HEAT_MAP = []

    @classmethod
    def _minimax(cls, node, alpha, beta, depth, maximizing_player) -> Result:
        if depth == 0 or node.is_terminal:
            return Result(value=node.value)
        if maximizing_player:
            result = Result(value=-INFINITY)
            for child, move, undo_move in node.children:
                (row, col) = move
                minimax_result = cls._minimax(child, alpha, beta, depth-1, False)
                minimax_result.value *= (-cls.HEAT_MAP[row][col])
                alpha = max(alpha, result.value)
                undo_move()
                if minimax_result.value >= result.value:
                    result = minimax_result
                    result.move = move
                if beta <= alpha:
                    break
            return result
        else:
            result = Result(value=INFINITY)
            for child, move, undo_move in node.children:
                (row, col) = move
                minimax_result = cls._minimax(child, alpha, beta, depth-1, True)
                minimax_result.value *= cls.HEAT_MAP[row][col]
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
        if not cls.HEAT_MAP:
            cls.init_heat_map(game_field)

        initial_node = cls.NODE(game_field, player_color)
        result = cls._minimax(initial_node, -INFINITY, INFINITY, cls.DEPTH, True)
        move = result.move
        if not move and initial_node.available_moves:
            move = random.choice(initial_node.available_moves)

        return move
    
    @classmethod
    def init_heat_map(cls, game_field):
        cls.HEAT_MAP = [
            [0.01, 1.2, 0.7, 0.5, 0.5, 0.7, 1.2,  0.01],
            [1.2,  1.5,  0.6, 0.8,   0.8,  0.6, 1.5, 1.2],
            [0.7, 0.6, 0.8,   1,   1, 0.8,  0.6,  0.7],
            [0.5, 0.8,   1,   1,   1,   1,  0.8,  0.5],
            [0.5, 0.8,   1,   1,   1,   1,  0.8,  0.5],
            [0.7, 0.6, 0.8,   1,   1, 0.8,  0.6,  0.7],
            [1.2, 1.5,  0.6, 0.8, 0.8, 0.6, 1.5, 1.2],
            [0.01, 1.2, 0.7, 0.5, 0.5, 0.7, 1.2,  0.01]
        ]

        for row in cls.HEAT_MAP:
            for cell in row:
                cell = math.sqrt(cell)

        if game_field.black_hole is not None:
            (row, col) = game_field.black_hole
            field_row_len = len(game_field.field)
            field_col_len = len(game_field.field[0])

            def is_in_field(row, col):
                return row >= 0 and col >= 0 and (row <= field_row_len - 1) and (col <= field_col_len - 1)
            if row == 0 or col == 0 or row == field_row_len - 1 or col == field_col_len - 1: 
                for (dx, dy) in [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]:
                    if is_in_field(row+dx, col+dy):
                        cls.HEAT_MAP[row+dx][col+dy] = 0.01