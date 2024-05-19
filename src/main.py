import pygame as pg
import colony


class Game:
    def __init__(self, resolution: tuple, frame_rate: int) -> None:
        pg.init()
        self.screen = pg.display.set_mode(resolution)
        self.clock = pg.time.Clock()
        self.running = True 
        self.frame_rate = frame_rate

    def main(self) -> None:
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                self.screen.fill("purple")

                pg.display.flip() 

            self.clock.tick(self.frame_rate)
        
        pg.quit()


game_of_life = Game((1280, 720), 1)
game_of_life.main()