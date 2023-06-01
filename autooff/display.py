import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class OLEDDisplay:
    FONT: ClassVar[str] = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    FONT_14: ClassVar[ImageFont.FreeTypeFont] = ImageFont.truetype(FONT, 14)
    FONT_28: ClassVar[ImageFont.FreeTypeFont] = ImageFont.truetype(FONT, 28)

    DEVICE_ADDR: int = field(default=0x3C)
    DISPLAY_WIDTH: int = field(default=128)
    DISPLAY_HEIGHT: int = field(default=64)

    def __post_init__(self):
        self.oled = None
        self.image = None
        self.draw = None
        self._init()

    def _init(self):
        RESET_PIN = digitalio.DigitalInOut(board.D4)
        i2c = board.I2C()
        self.oled = adafruit_ssd1306.SSD1306_I2C(
            width=self.DISPLAY_WIDTH,
            height=self.DISPLAY_HEIGHT,
            i2c=i2c,
            addr=self.DEVICE_ADDR,
            reset=RESET_PIN
        )
        self.image = Image.new("1", (self.oled.width, self.oled.height))
        self.draw = ImageDraw.Draw(self.image)

    def show(self):
        self.draw.text((0, 30), "Hello!", font=self.FONT_14, fill=255)
        self.oled.image(self.image)
        self.oled.show()

    def reset(self):
        self.oled.fill(0)
        self.oled.show()


d = OLEDDisplay()
d.show()

import time
time.sleep(3)

d.reset()