import pygame as pg

# pg setup
pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
running = True
test_rectangle = pg.Rect(16, 16, 16, 16)
while running:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    pg.draw.rect(screen, "red", test_rectangle)
    # flip() the display to put your work on screen
    pg.display.flip()

    clock.tick(10)  # limits FPS to 60

pg.quit()
