import cell
import numpy as np


class Colony:
    def __init__(self, screen_width: int, screen_height: int):
        self.rows = self.__calculate_rows(screen_height)
        self.columns = self.__calculate_columns(screen_width)
        self.bit_map = self.__initiate_bit_map(self.rows, self.columns)

    def __calculate_rows(self, screen_height: int) -> int:
        return int(screen_height / 16)

    def __calculate_columns(self, screen_width: int) -> int:
        return int(screen_width / 16)

    def __initiate_bit_map(self, rows: int, columns: int) -> np.ndarray:
        bit_map = np.zeros((rows, columns), dtype=cell.Cell)
        for i in range(rows):
            for j in range(columns):
                bit_map[i][j] = cell.Cell(i, j)
                if i == 0 or j == 0:
                    bit_map[i][j].is_boarder = True
                elif i == rows - 1 or j == columns - 1:
                    bit_map[i][j].is_boarder = True

        return bit_map

    def get_cell(self, row: int, column: int) -> cell.Cell:
        return self.bit_map[row][column]

    def resurect_cell_at(self, row: int, column: int) -> None:
        self.get_cell(row, column).resurect_cell()

    def kill_cell_at(self, row: int, column: int) -> None:
        self.get_cell(row, column).kill_cell()

    def find_num_alive_neighbors(self, row: int, column: int) -> int:
        count = 0
        neighbor_matrix = np.array([])

        # top left
        if row == 0 and column == 0:
            neighbor_matrix = self.bit_map[row:row+2, column:column+2]
            neighbor_matrix = neighbor_matrix.flatten()
            neighbor_matrix = np.delete(neighbor_matrix, 0)

        # top right
        elif row == 0 and column == self.columns-1:
            neighbor_matrix = self.bit_map[row:row+2, column-1:column+1]
            neighbor_matrix = neighbor_matrix.flatten()
            neighbor_matrix = np.delete(neighbor_matrix, 1)

        elif row == self.rows-1 and column == 0:
            pass

        elif row == self.rows-1 and column == self.columns-1:
            pass

        elif row == 0:
            pass

        elif column == 0:
            pass

        else:
            neighbor_matrix = self.bit_map[row-1:row+2, column-1:column+2]
            neighbor_matrix = neighbor_matrix.flatten()
            neighbor_matrix = np.delete(neighbor_matrix, 4)

        for tile in neighbor_matrix:
            if tile.is_alive:
                count = count + 1

        return count
