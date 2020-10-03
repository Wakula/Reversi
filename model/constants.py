import enum

class Player(enum.Enum):
    BLACK = '*'
    WHITE = '+'
    EMPTY = '0'

class Directions(enum.Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UPLEFT = 'UPLEFT'
    UPRIGHT = 'UPRIGHT'
    DOWNLEFT = 'DOWNLEFT'
    DOWNRIGHT = 'DOWNRIGHT'