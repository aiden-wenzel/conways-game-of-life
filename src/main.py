import pygame as pg
import colony


class Game:
    def __init__(self, resolution: tuple, frame_rate: int) -> None:
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.running = True 
        self.frame_rate = frame_rate
        self.colony = colony.Colony(resolution[0], resolution[1])

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
        self.screen.fill("purple")

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                self.draw_colony()

                pg.display.flip() 

            self.clock.tick(self.frame_rate)
        
        pg.quit()


game_of_life = Game((1280, 720), 10)
game_of_life.main()