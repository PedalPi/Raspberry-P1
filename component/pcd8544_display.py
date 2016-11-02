from physical.component.pcd8544.pcd8544 import PCD8544
from PIL import ImageFont

class PCD8544Display(object):

    def __init__(self, dc, sclk, din, cs, rst, contrast):
        self.display = PCD8544(dc=dc, sclk=sclk, din=din, cs=cs, rst=rst, contrast=contrast, inverse=False)

    def show_patch(self, patch):
        font_index = ImageFont.truetype('FreeSansBold.ttf', size=35)
        font_name = ImageFont.truetype('FreeSans.ttf', size=15)

        index = '{:02d}'.format(patch.index)

        print(index, '-', patch["name"])

        self.display.clear()
        self._draw_center_text(index, font_index, -5)

        display_height = self.display.height

        text_position = ((0, 2*display_height/3), (self.display.width, display_height))
        self.display.draw.rectangle(text_position, outline=0, fill=1)
        self._draw_center_text(patch["name"], font_name, text_position[0][1], fill=0)

        self.display.dispose()

    def _draw_center_text(self, text, font, y, fill=1):
        position = self._center_text(text, font, y)
        self.display.draw.text(position, text, font=font, fill=fill)

    def _center_text(self, text, font, y):
        size = font.getsize(text)
        x = (self.display.width - size[0]) / 2

        return x, y

    def show_effect(self, effect):
        pass

    def show_param(self, param):
        pass
