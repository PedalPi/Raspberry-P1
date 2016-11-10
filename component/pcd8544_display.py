from physical.component.pcd8544.pcd8544 import PCD8544
from PIL import ImageFont


class PCD8544Display(object):

    def __init__(self, dc, sclk, din, cs, rst, contrast):
        self.display = PCD8544(dc=dc, sclk=sclk, din=din, cs=cs, rst=rst, contrast=contrast, inverse=False)
        self.drawer = Drawer(self.display)

    @property
    def font_header(self):
        return ImageFont.truetype('FreeSans.ttf', size=10)

    def font_footer(self, size=12):
        return ImageFont.truetype('FreeSans.ttf', size=size)

    def show_patch(self, patch):
        font_index = ImageFont.truetype('FreeSansBold.ttf', size=35)

        index = '{:02d}'.format(patch.index)

        self.display.clear()

        self.drawer.center_text(index, font_index, -5)
        self.drawer.footer(patch['name'], self.font_footer(15))

        self.display.dispose()

    def show_effect(self, effect):
        patch = effect.patch

        font_index = ImageFont.truetype('FreeSansBold.ttf', size=25)

        index = '{:02d}'.format(patch.index)

        self.display.clear()

        self.drawer.header(' ' + index + ' - ' + patch['name'], self.font_header)
        self.drawer.center_text(str(effect.index + 1), font_index, self.display.height/5, fill=1)
        self.drawer.footer(effect['name'], self.font_footer())

        self.display.dispose()

    def show_param(self, param):
        effect = param.effect
        header = '{:02d} {}'.format(effect.index, effect['name'])

        self.display.clear()
        self.drawer.header(header, self.font_header)
        self.draw_param_range(param)
        self.drawer.footer(param['name'], self.font_footer())
        self.display.dispose()

    def draw_param_range(self, param):
        bar_size = self.display.width*4/5, self.display.height/8

        rectangle = (
            (self.display.width/10,   self.display.height/2 - bar_size[1]/2),
            (self.display.width*9/10, self.display.height/2 + bar_size[1]/2)
        )

        rectangle_value = (
            rectangle[0],
            (self._range_rectangle_width(param) + self.display.width/10, rectangle[1][1])
        )

        self.display.draw.rectangle(rectangle, outline=1, fill=0)
        self.display.draw.rectangle(rectangle_value, outline=1, fill=1)

    def _range_rectangle_width(self, param):
        minimum = param['ranges']['minimum']
        maximum = param['ranges']['maximum']
        bar = self.display.width * 8/10
        value = param.value

        return bar*(value - minimum)/(maximum - minimum)


class Drawer(object):

    def __init__(self, display):
        self.display = display

    def center_text(self, text, font, y, fill=1):
        position = self._center_text(text, font, y)
        self.display.draw.text(position, text, font=font, fill=fill)

    def _center_text(self, text, font, y):
        size = font.getsize(text)
        x = (self.display.width - size[0]) / 2

        return x, y

    def header(self, text, font):
        text_position = ((0, 0), (self.display.width, font.getsize(text)[1]))

        self.display.draw.rectangle(text_position, outline=1, fill=1)
        self.display.draw.text(text_position[0], text, font=font, fill=0)

    def footer(self, text, font):
        text_height = font.getsize(text)[1]
        display_height = self.display.height

        text_position = ((0, display_height - text_height), (self.display.width, display_height))
        self.display.draw.rectangle(text_position, outline=1, fill=1)
        self.center_text(text, font, text_position[0][1], fill=0)
