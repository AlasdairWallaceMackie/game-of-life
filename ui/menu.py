import pyxel
from . import UIObject

MENU_TEXT = """
   Conway's
 Game of Life

SPACE - Pause
    C - Clear
    M - Menu
"""

class Menu(UIObject):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.w = 64
    self.h = 56

  def draw(self):
    # Border
    pyxel.rect(
      self.x, self.y,
      self.w, self.h,
      pyxel.COLOR_NAVY
    )
    # Main
    pyxel.rect(
      self.x+1, self.y+1,
      self.w - 2, self.h - 2,
      pyxel.COLOR_DARK_BLUE
    )

    pyxel.text(
      self.x + 4, self.y + 4,
      MENU_TEXT,
      pyxel.COLOR_WHITE
    )
