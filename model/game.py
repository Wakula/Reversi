import * from constants

class Game:
    _field = []
    _current_player = Player.Black
    _side_length = 8

    def __init__():
        _init_field()


    def _init_field():
        _field = [[Cell.Empty] * _side_length for i in range(_side_length)]

        half_length = _side_length / 2

        _field[half_length][half_length] = _field[half_length + 1][half_length + 1] = Cell.White
        _field[half_length][half_length + 1] = _field[half_length + 1][half_length] = Cell.Black