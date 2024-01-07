import pyxel
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_COLOR
import ui

class Game:

  def __init__(self):
    self.grid = self.get_blank_grid()

    self.paused = True

    self.ui_elements = [
      ui.PlayButton(2, 2, on_click=self.toggle_pause_game),
      ui.ClearButton(WINDOW_WIDTH - pyxel.TILE_SIZE - 1, 2, on_click=self.reset_grid),
    ]

  def update(self):
    self.update_ui()

    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and is_mouse_in_window():
      self.toggle_cell(pyxel.mouse_x, pyxel.mouse_y)

  def draw(self):
    self.draw_cells()
    self.draw_ui()
    self.draw_pause_symbol(2, WINDOW_HEIGHT - pyxel.TILE_SIZE - 2)

  ######################

  def toggle_pause_game(self):
    self.paused ^= True

  def toggle_cell(self, x, y):
    self.grid[x][y] ^= 1

  def get_blank_grid(self):
    new_grid = []

    for x in range(WINDOW_WIDTH):
      new_grid.append([0 for y in range(WINDOW_HEIGHT)])

    return new_grid

  def reset_grid(self):
    self.grid = self.get_blank_grid()

  def update_ui(self):
    for element in self.ui_elements:
      element.update()

  def draw_cells(self):
    for x in range(WINDOW_WIDTH):
      for y in range(WINDOW_HEIGHT):
        if self.grid[x][y]:
          pyxel.pset(x, y, CELL_COLOR)

  def draw_ui(self):
    for element in self.ui_elements:
      element.draw()

  def draw_pause_symbol(self, x, y):
    if self.paused:
      pyxel.blt(
        x, y,
        0,
        0, pyxel.TILE_SIZE * 2,
        pyxel.TILE_SIZE, pyxel.TILE_SIZE,
        pyxel.COLOR_BLACK
      )

########
########

def is_mouse_in_window():
  return (0 <= pyxel.mouse_x < WINDOW_WIDTH) and (0 <= pyxel.mouse_y < WINDOW_HEIGHT)
