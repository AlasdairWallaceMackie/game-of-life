import pyxel
import ui
from cursor import Cursor
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, CELL_COLOR

class Game:

  def __init__(self):
    self.grid = self.get_blank_grid()

    self.paused = True

    self.ui_elements = [
      ui.PlayButton(2, 2, on_click=self.toggle_pause_game),
      ui.ClearButton(WINDOW_WIDTH - pyxel.TILE_SIZE - 1, 2, on_click=self.reset_grid),
    ]

    self.cursor = Cursor()

  def update(self):
    self.update_ui()
    if not self.paused:
      self.update_cells()

    if pyxel.btnp(pyxel.KEY_SPACE, 9999, 9999):
      self.toggle_pause_game()

    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and is_mouse_in_window():
      self.grid[pyxel.mouse_x][pyxel.mouse_y] = True

  def draw(self):
    self.draw_cells()
    self.draw_ui()
    self.draw_pause_symbol(2, WINDOW_HEIGHT - pyxel.TILE_SIZE - 2)
    self.cursor.draw(pyxel.mouse_x, pyxel.mouse_y, is_hovering_ui=self.is_cursor_hovering_ui())

  ######################

  def toggle_pause_game(self):
    self.paused ^= True

  def toggle_cell(self, x, y):
    self.grid[x][y] ^= True

  def get_blank_grid(self):
    new_grid = []

    for x in range(WINDOW_WIDTH):
      new_grid.append([False for y in range(WINDOW_HEIGHT)])

    return new_grid

  def reset_grid(self):
    self.grid = self.get_blank_grid()

  def update_cells(self):
    new_grid = self.get_blank_grid()

    for x in range(len(self.grid)):
      for y in range(len(self.grid[x])):
        neighbor_count = self.get_cell_neighbor_count(x, y)
        cell_alive = self.grid[x][y]

        if cell_alive:
          """
          Any live cell with fewer than two live neighbors dies, as if by underpopulation.
          Any live cell with two or three live neighbors lives on to the next generation.
          Any live cell with more than three live neighbors dies, as if by overpopulation.
          """
          new_grid[x][y] = not neighbor_count < 2 and not neighbor_count > 3
        elif neighbor_count == 3:
          """
          Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
          """
          new_grid[x][y] = True

    self.grid = new_grid

  def get_cell_neighbor_count(self, x, y):
    count = 0
    
    for nx, ny in [
      (x-1, y),
      (x-1, y-1),
      (x-1, y+1),
      (x+1, y),
      (x+1, y-1),
      (x+1, y+1),
      (x, y-1),
      (x, y+1),
    ]:
      if not 0 < nx < WINDOW_WIDTH - 1 or not 0 < ny < WINDOW_HEIGHT - 1:
        continue

      if self.grid[nx][ny]:
        count += 1

    return count

  def update_ui(self):
    for element in self.ui_elements:
      element.update()

  def is_cursor_hovering_ui(self):
    for element in self.ui_elements:
      if element.is_mouse_hovered():
        return True

    return False

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
