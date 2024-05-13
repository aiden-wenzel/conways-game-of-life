import cell
import numpy as np


class Colony:
    def __init__(self, screen_width: int, screen_height: int):
        self.rows = self.__calculate_rows(screen_height)
        self.columns = self.__calculate_columns(screen_width)
        self.bit_map = self.__initiate_bit_map(self.columns, self.rows)

    def __calculate_rows(self, screen_height: int) -> int:
        return int(screen_height / 16)

    def __calculate_columns(self, screen_width: int) -> int:
        return int(screen_width / 16)

    def __initiate_bit_map(self, columns: int, rows: int) -> np.ndarray:
        bit_map = np.zeros((rows, columns), dtype=cell.Cell)
        for i in range(rows):
            for j in range(columns):
                bit_map[i][j] = cell.Cell(i, j)

        return bit_map

    def get_cell(self, row: int, column: int) -> cell.Cell:
        return self.bit_map[row][column]

    def resurect_cell_at(self, row: int, column: int) -> None:
        self.get_cell(row, column).resurect_cell()
