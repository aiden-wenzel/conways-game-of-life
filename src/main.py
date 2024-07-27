"""The main driver file of this program."""

import pygame as pg
import colony
import plotter
import button


class Game:
    def __init__(self, resolution: tuple, frame_rate: int) -> None:
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.running = True
        self.frame_rate = frame_rate
        self.colony = colony.Colony(resolution[0], resolution[1])
        self.selected_cell = None
        self.plot = plotter.Plotter()

    def draw_colony(self) -> None:
        for row in range(self.colony.rows):
            for column in range(self.colony.columns):
                color = ""
                if self.colony.get_cell(row, column).is_alive:
                    color = "black"
                elif self.colony.get_cell(row, column) == self.selected_cell:
                    color = "grey"
                else:
                    color = "white"

                pg.draw.rect(
                        self.screen,
                        color,
                        pg.Rect(self.colony.get_cell(row, column).calculate_screen_coordinates(),
                        (16, 16))
                )

    def _draw_button(self, left_corner: tuple, dimensions: tuple, color: str) -> None:
        button_to_draw = pg.Rect(left_corner, dimensions)
        pg.draw.rect(self.screen, color, button_to_draw)


    def main(self) -> None:
        in_gui = True
        in_game = False

        start_button = button.Button((0,0), (50, 25), "green")
        restart_button = button.Button((1280-50, 0), (50, 25), "red")

        self.screen.fill("purple")

        while self.running:

            # Exit the loop if the the player quits.
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            # Entry point to select cells
            if in_gui:

                # Render buttons.
                self.draw_colony()
                start_button.draw_button(self.screen)
                restart_button.draw_button(self.screen)

                # Determine the cell under the cursor.
                mouse_pos = pg.mouse.get_pos()
                mouse_row = int(mouse_pos[0]/16)
                mouse_column = int(mouse_pos[1]/16)
                self.selected_cell = self.colony.get_cell(mouse_column, mouse_row)

                # Determine if left mouse button is clicked.
                mouse_clicked = pg.mouse.get_pressed()
                left_clicked = mouse_clicked[0]

                if start_button.handle_cursor(mouse_pos):
                    in_gui = False
                    in_game = True
                    self.selected_cell.kill_cell()

                if left_clicked:
                    self.selected_cell.resurect_cell()

                pg.display.flip()


            elif in_game:
                self.draw_colony()
                start_button.draw_button(self.screen)
                restart_button.draw_button(self.screen)

                mouse_pos = pg.mouse.get_pos()
                mouse_clicked = pg.mouse.get_pressed()

                if restart_button.handle_cursor(mouse_pos):
                    self.colony.wipe_colony()
                    in_gui = True
                    in_game = False


                pg.display.flip()

                self.plot.update_cell_count_list(self.colony)
                self.colony.bit_map_determine_fate()
                self.colony.kill_and_resurect_cells()


            self.clock.tick(self.frame_rate)
        pg.quit()
        self.plot.save_plot()


game_of_life = Game((1280, 720), 30)
game_of_life.main()
