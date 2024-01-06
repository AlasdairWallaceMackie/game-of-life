import pyxel
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_COLOR

class Game:
  def __init__(self):
    self.grid = []
    self.reset_grid()

  def update(self):
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and mouse_in_window():
      self.grid[pyxel.mouse_x][pyxel.mouse_y] = 1

  def draw(self):
    for x in range(WINDOW_WIDTH):
      for y in range(WINDOW_HEIGHT):
        if self.grid[x][y]:
          pyxel.pset(x, y, CELL_COLOR)

  def reset_grid(self):
    self.grid = []

    for x in range(WINDOW_WIDTH):
      self.grid.append([0 for y in range(WINDOW_HEIGHT)])


def mouse_in_window():
  return (0 <= pyxel.mouse_x < WINDOW_WIDTH) and (0 <= pyxel.mouse_y < WINDOW_HEIGHT)
