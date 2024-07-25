"""
This module contains the plotter class which will be used to track 
and plot the population of cells over the course of the game.
"""

import matplotlib.pyplot as plt
import numpy as np
import colony

class Plotter:
    """
    This is a class for the plotter object which is responsible for tracking 
    and displaying the population of cells over the course of the game.
    """

    def __init__(self) -> None:
        """
        Initialize the array which stores the population.
        """
        self.cell_array = np.array([])

    def count_alive_cells(self, colony_in: colony.Colony) -> int:
        """
        Return the number of alive cells in the colony.
        """

        num_alive_cells = 0

        for row in range(colony_in.rows):
            for column in range(colony_in.columns):
                if colony_in.get_cell(row, column).get_is_alive():
                    num_alive_cells += 1

        return num_alive_cells

    def update_cell_count_list(self, colony_in: colony.Colony) -> None:
        """
        Append the number of alive cells at the current ticket to self.cell_array.
        Call this function at the end of each tick.
        """

        tick_cell_count = self.count_alive_cells(colony_in)
        np.append(self.cell_array, tick_cell_count)

    def display_plot(self) -> None:
        """
        Display a plot of the number of alive cells vs tick.
        """

        plt.plot(self.cell_array)
