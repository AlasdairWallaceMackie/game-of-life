import pyxel
import controls
from . import UIObject

class PlayButton(UIObject):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.w = 7
    self.h = 8

  def draw(self):
    u = 1 * pyxel.TILE_SIZE if (self.is_mouse_clicked_hold() or pyxel.btn(controls.PAUSE)) else 0

    pyxel.blt(
      self.x, self.y,
      0,
      u, 0,
      self.w, self.h,
      pyxel.COLOR_BLACK
    )

    super().draw()
