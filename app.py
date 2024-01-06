import os, sys
import pyxel
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BACKGROUND_COLOR
from game import Game


class App:
  def __init__(self):
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
    pyxel.mouse(True)
    pyxel.load("sprites.pyxres")

    self.game = Game()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_GUI) and pyxel.btn(pyxel.KEY_R):
      print("RESTARTING")
      os.execv(sys.executable, ['pyxel'] + sys.argv)

    self.game.update()

  def draw(self):
    pyxel.cls(BACKGROUND_COLOR)
    self.game.draw()

App()
