class Cell:
    def __init__(self, row_in: int, column_in: int):
        """Initialize the cell as dead, at row_in and column_in,
        and initialize the screen coordinates of the cell"""


        self.is_alive = False
        self.is_highlighted = False
        self.is_boarder = False
        self.row = row_in
        self.column = column_in
        self.screen_coordinates = self.calculate_screen_coordinates()

    def get_is_alive(self) -> bool:
        """Return a bool indicating if the current cell is alive."""

        return self.is_alive

    def resurect_cell(self) -> None:
        """Change the cell to be alive."""

        self.is_alive = True

    def highlight_cell(self) -> None:
        """Change the cell to be highlighted while in GUI"""

        self.is_highlighted = True

    def kill_cell(self) -> None:
        """Change the cell to be dead."""

        self.is_alive = False

    def calculate_screen_coordinates(self) -> tuple:
        """Return the screen coordinates of the cell as a tuple (column, row)."""

        return (self.column*16, self.row*16)
