# coding=utf-8

"""
让一行字在图片居中 demo

environment:
* Linux/Windows
* python 3.6.*
* dependencies
    * make sure you have installed dependencies by command below before run the demo
    * pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
import string
import os

bg_size = (750, 1334)
bg = Image.new('RGB', bg_size, color=(255,255,255))

font_size = 36
text = '1lin24 is me. 我是1lin24。'

font_path = os.path.join('.', 'fonts', 'SourceHanSansCN-Medium.otf')
font = ImageFont.truetype(font_path, font_size)
text_width = font.getsize(text)
draw = ImageDraw.Draw(bg)

text_coordinate = int((bg_size[0]-text_width[0])/2), int((bg_size[1]-text_width[1])/2)
draw.text(text_coordinate, text,(0,0,0), font=font)

img_path = os.path.join('.', 'output', 'center_text.jpg')
bg.save(img_path)
print('保存成功 at {}'.format(img_path))

# GUI 可以使用下面的方式 直接查看效果
# bg.show()