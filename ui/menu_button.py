import pyxel
import controls
from . import UIObject

class MenuButton(UIObject):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.w = 8
    self.h = 8

  def draw(self):
    u = 1 * pyxel.TILE_SIZE if (self.is_mouse_clicked_hold() or pyxel.btn(controls.MENU)) else 0

    pyxel.blt(
      self.x, self.y,
      0,
      u, 3 * pyxel.TILE_SIZE,
      self.w, self.h,
      pyxel.COLOR_BLACK
    )

    super().draw()
