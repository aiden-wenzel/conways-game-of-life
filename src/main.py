import pygame as pg
import logging as log
import utils
import colony


logger = log.getLogger(__name__)
logger.setLevel(log.DEBUG)

class Game:
    def __init__(self, resolution: tuple, frame_rate: int) -> None:
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.running = True 
        self.frame_rate = frame_rate
        self.colony = colony.Colony(resolution[0], resolution[1])
        self.selected_cell = None

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
                
                pg.draw.rect(self.screen, color, pg.Rect(self.colony.get_cell(row, column).calculate_screen_coordinates(), (16, 16)))

    def _draw_button(self, left_corner: tuple, dimensions: tuple, color: str) -> None:
        button = pg.Rect(left_corner, dimensions)
        pg.draw.rect(self.screen, color, button)

    def _button_hover(self, mouse_pos: tuple, button_pos: tuple, button_dimensions: tuple) -> bool:
        button_height = button_dimensions[1]
        button_width = button_dimensions[0]

        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        in_width = mouse_x > button_pos[0] and mouse_x < button_pos[0] + button_width
        in_height = mouse_y > button_pos[1] and mouse_y < button_pos[1] + button_height

        return in_width and in_height




    def main(self) -> None:
        in_gui = True
        in_game = False

        self.screen.fill("purple")

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            if in_gui:
                self.draw_colony()
                self._draw_button((0, 0), (50, 25), "red")
                self._draw_button((1280-50, 720-25), (50, 25), "green")
                mouse_pos = pg.mouse.get_pos()
                mouse_row = int(mouse_pos[0]/16)
                mouse_column = int(mouse_pos[1]/16)
                self.selected_cell = self.colony.get_cell(mouse_column, mouse_row)

                mouse_clicked = pg.mouse.get_pressed()
                left_clicked = mouse_clicked[0]

                if left_clicked and self._button_hover(mouse_pos, (0, 0), (50, 25)):
                    in_gui = False
                    in_game = True
                    self.selected_cell.kill_cell()  

                if left_clicked:
                    self.selected_cell.resurect_cell()

                pg.display.flip()
                


            elif in_game:
                mouse_pos = pg.mouse.get_pos()
                self.draw_colony()
                self._draw_button((0, 0), (50, 25), "red")
                self._draw_button((1280-50, 720-25), (50, 25), "green")
                mouse_clicked = pg.mouse.get_pressed()
                left_clicked = mouse_clicked[0]

                if left_clicked and self._button_hover(mouse_pos, (1280-50, 720-25), (50, 25)):
                    # Clear screen
                    # go back to gui
                    self.colony.wipe_colony()
                    in_gui = True
                    in_game = False


                pg.display.flip() 

                self.colony.bit_map_determine_fate()
                self.colony.kill_and_resurect_cells()        

       

            self.clock.tick(self.frame_rate)
        pg.quit()


game_of_life = Game((1280, 720), 10)
game_of_life.main()
