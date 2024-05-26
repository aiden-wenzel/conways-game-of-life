import pygame as pg
import pygame_gui as gui
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
        self.colony.initiate_live_cells(utils.read_pattern("../patterns/alef.csv"))

    def draw_colony(self) -> None:
        for row in range(self.colony.rows):
            for column in range(self.colony.columns):
                color = ""
                if self.colony.get_cell(row, column).is_alive:
                    color = "black"
                else:
                    color = "white"
                
                pg.draw.rect(self.screen, color, pg.Rect(self.colony.get_cell(row, column).calculate_screen_coordinates(), (16, 16)))

    def main(self) -> None:
        logger.debug("Entering main")

        in_gui = True
        in_game = False

        self.screen.fill("purple")

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            if in_gui:
                self.screen.fill("red")
                pg.display.flip()

            elif in_game:

                self.draw_colony()
                pg.display.flip() 

                self.colony.bit_map_determine_fate()
                self.colony.kill_and_resurect_cells()        

       

            self.clock.tick(self.frame_rate)
        pg.quit()


game_of_life = Game((1280, 720), 10)
game_of_life.main()
