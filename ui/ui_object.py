import pyxel
import constants

class UIObject:

  border_padding = 2

  def __init__(
    self,
    x, y,
    on_hover=lambda *args, **kwargs: None,
    on_click=lambda *args, **kwargs: None,
  ):
    self.x = x
    self.y = y

    self.w = pyxel.TILE_SIZE
    self.h = pyxel.TILE_SIZE
    
    self.on_hover = on_hover
    self.on_click = on_click

  def update(self):
    if self.is_mouse_clicked():
      self.on_click()

  def draw(self):
    if self.is_mouse_hovered():
      self.on_hover()
      self.draw_border()
      
  ###########################

  def is_mouse_hovered(self):
    return (self.x <= pyxel.mouse_x < self.x + self.w) and (self.y <= pyxel.mouse_y < self.y + self.h)
  
  def is_mouse_clicked(self):
    return pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT, 9999, 9999) and self.is_mouse_hovered()
  
  def is_mouse_clicked_hold(self, ):
    return pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.is_mouse_hovered()

  def draw_border(self):
    # self.draw_border_shadow()

    pyxel.rectb(
      self.border_x(), self.border_y(),
      self.border_w(), self.border_h(),
      constants.UI_HIGHLIGHT_COLOR
    )

  def draw_border_shadow(self):
    pyxel.rectb(
      self.border_x(), self.border_y() + 1,
      self.border_w(), self.border_h(),
      constants.UI_SHADOW_COLOR
    )

  def border_x(self):
    return self.x - self.border_padding
  
  def border_y(self):
    return self.y - self.border_padding

  def border_w(self):
    return self.w + (self.border_padding * 2)

  def border_h(self):
    return self.h + (self.border_padding * 2)
