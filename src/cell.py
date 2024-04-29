class Cell:
    def __init__(self, row_in: int, column_in: int):
        self.is_alive: bool = False
        self.row: int = row_in
        self.column: int = column_in 
        
