import pyxel
import constants

class Cursor:
  def __init__(self):
    self.current_brush = "pixel"

  def update(self):
    pass

  def draw(self, x, y):
    if self.current_brush == "pixel":
      pyxel.pset(x, y, constants.CELL_COLOR)
