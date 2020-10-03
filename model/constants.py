import enum


class Player(enum.Enum):
    BLACK = 'black'
    WHITE = 'white'
    NONE = 'none'


class Cell(enum.Enum):
    BLACK = '*'
    WHITE = '+'
    EMPTY = '0'
