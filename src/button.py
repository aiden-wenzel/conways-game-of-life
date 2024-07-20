import pygame as pg

class Button:
    def __init__(self, position: tuple, dimensions: tuple, color: str) -> None:
        self.position = position
        self.dimensions = dimensions
        self.color = color
        self.shape = pg.Rect(position, dimensions)

    def draw_button(self, screen: pg.Surface) -> None:
        pg.draw.rect(screen, self.color, self.shape)

    def _button_hover(self, mouse_pos: tuple) -> bool:
        button_height = self.dimensions[1]
        button_width = self.dimensions[0]

        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        in_width = mouse_x > self.position[0] and mouse_x < self.position[0] + button_width
        in_height = mouse_y > self.position[1] and mouse_y < self.position[1] + button_height

        return in_width and in_height

    def handle_cursor(self, mouse_pos: tuple) -> bool:
        mouse_clicked = pg.mouse.get_pressed()
        left_clicked = mouse_clicked[0]

        return left_clicked and self._button_hover(mouse_pos)


