class Cell:
    def __init__(self, row_in: int, column_in: int):
        self.is_alive = False
        self.is_boarder = False
        self.row = row_in
        self.column = column_in

    def get_is_alive(self) -> bool:
        return self.is_alive

    def resurect_cell(self) -> None:
        self.is_alive = True

    def kill_cell(self) -> None:
        self.is_alive = False
