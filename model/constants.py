import enum

class Player(enum.Enum):
    BLACK = 'B'
    WHITE = 'W'
    EMPTY = ' '

class Directions(enum.Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    UPLEFT = 'UPLEFT'
    UPRIGHT = 'UPRIGHT'
    DOWNLEFT = 'DOWNLEFT'
    DOWNRIGHT = 'DOWNRIGHT'