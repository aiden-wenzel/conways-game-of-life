class Cell:
    def __init__(self, row_in: int, column_in: int):
        self.is_alive = False
        self.row = row_in
        self.column = column_in

    def get_is_alive(self):
        return self.is_alive
