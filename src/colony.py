import numpy as np

class Colony:
    def __init__(self, screen_width: int, screen_height: int):
        self.rows = self.__calculate_rows__(screen_height)
        self.columns = self.__calculate_columns__(screen_width)
        self.bit_map = None  # TODO: write bit_map initiation

    def __calculate_rows__(self, screen_height: int) -> int:
        return screen_height / 16

    def __calculate_columns__(self, screen_width: int) -> int:
        return screen_width / 16

    def __initiate_bit_map__(self, columns: int, rows: int) -> np.ndarray:
        return np.zeros((columns, rows))
