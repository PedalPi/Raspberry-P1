from physical.component.pcd8544.pcd8544 import PCD8544
from PIL import ImageFont

class PCD8544Display(object):

    def __init__(self, dc, sclk, din, cs, rst, contrast):
        self.display = PCD8544(dc=dc, sclk=sclk, din=din, cs=cs, rst=rst, contrast=contrast, inverse=False)

    def show_patch(self, patch):
        font_index = ImageFont.truetype('FreeSansBold.ttf', size=35)
        font_name = ImageFont.truetype('FreeSans.ttf', size=15)

        index = '{:02d}'.format(patch.index)

        self.display.clear()

        self._draw_center_text(index, font_index, -5)
        self._draw_footer(patch['name'], font_name)

        self.display.dispose()

    def _draw_center_text(self, text, font, y, fill=1):
        position = self._center_text(text, font, y)
        self.display.draw.text(position, text, font=font, fill=fill)

    def _center_text(self, text, font, y):
        size = font.getsize(text)
        x = (self.display.width - size[0]) / 2

        return x, y

    def show_effect(self, effect):
        patch = effect.patch

        font_patch = ImageFont.truetype('FreeSans.ttf', size=10)
        font_index = ImageFont.truetype('FreeSansBold.ttf', size=25)
        font_effect = ImageFont.truetype('FreeSans.ttf', size=12)

        self.display.clear()

        index = '{:02d}'.format(patch.index)
        self._draw_header(' ' + index + ' - ' + patch['name'], font_patch)
        self._draw_center_text(str(effect.index + 1), font_index, self.display.height/5, fill=1)
        self._draw_footer(effect['name'], font_effect)

        self.display.dispose()

    def _draw_header(self, text, font):
        text_position = ((0, 0), (self.display.width, font.getsize(text)[1]))

        self.display.draw.rectangle(text_position, outline=0, fill=1)
        self.display.draw.text(text_position[0], text, font=font, fill=0)

    def _draw_footer(self, text, font):
        text_height = font.getsize(text)[1]
        display_height = self.display.height

        text_position = ((0, display_height-text_height), (self.display.width, display_height))
        self.display.draw.rectangle(text_position, outline=0, fill=1)
        self._draw_center_text(text, font, text_position[0][1], fill=0)

    def show_param(self, param):
        pass
