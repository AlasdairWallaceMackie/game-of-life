import pyxel
import constants

class Cursor:
  def __init__(self):
    self.current_brush = "pixel"

  def update(self):
    pass

  def draw(self, x, y, is_hovering_ui=False):
    if is_hovering_ui:
      self.draw_hand(x, y)
      return

    if self.current_brush == "pixel":
      pyxel.pset(x, y, constants.CELL_COLOR)

  ####################
      
  def draw_hand(self, x, y):
    pyxel.blt(
        x, y,
        0,
        pyxel.TILE_SIZE * 2, 0,
        pyxel.TILE_SIZE, pyxel.TILE_SIZE,
        pyxel.COLOR_BLACK
    )
