from pygame import draw

class bricks:
    def __init__(self) -> None:
        pass


class bar:
    def __init__(self, screen, pos_x, pos_y, color, width, height) -> None:
        self._screen = screen
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._color = color
        self._width = width
        self._height = height

    def draw():
        pass
        # draw.rect(screen, white, (pos_x, pos_y, self._width, self._height), 0)