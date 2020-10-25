from typing import Tuple, Optional


class InputMapper:
    Y_MAPPING_TO_COORDINATES = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
    }
    Y_COORDINATES_TO_MAPPING = {
        coordinate: mapping for mapping, coordinate in Y_MAPPING_TO_COORDINATES.items()
    }

    @classmethod
    def get_x(cls, x_mapping: str) -> int:
        return int(x_mapping) - 1

    @classmethod
    def get_y(cls, y_mapping: str) -> int:
        return cls.Y_MAPPING_TO_COORDINATES[y_mapping]

    @classmethod
    def get_x_mapping(cls, x: int) -> str:
        return str(x + 1)

    @classmethod
    def get_y_mapping(cls, y: int) -> str:
        return cls.Y_COORDINATES_TO_MAPPING[y]

    @classmethod
    def get_coordinates(cls, input_: str) -> Optional[Tuple[int, int]]:
        try:
            y, x = tuple(input_)
        except ValueError:
            return None
        return cls.get_x(x), cls.get_y(y)

    @classmethod
    def get_mapping(cls, coordinates: Optional[Tuple[int, int]]) -> str:
        if not coordinates:
            return 'pass'
        x, y = coordinates
        y_mapping = cls.get_y_mapping(y)
        x_mapping = cls.get_x_mapping(x)
        return f"{y_mapping}{x_mapping}"
