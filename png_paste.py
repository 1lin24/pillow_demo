# coding=utf-8

"""
粘贴带透明背景的png图片 demo

environment:
* Linux/Windows
* python 3.6.*
* dependencies
    * make sure you have installed dependencies by command below before run the demo
    * pip install Pillow
"""

from PIL import Image, ImageDraw
import os

bg_size = (750, 1334)
bg = Image.new('RGBA', bg_size, color=(255,255,255,255))

fruit_size = (120, 100)
fruit_path = os.path.join('.', 'imgs', 'fruits.png')
fruit = Image.open(fruit_path).convert('RGBA')
x, y = int((bg_size[0]-fruit_size[0])/2), int((bg_size[1]-fruit_size[1])/2)
fruit_box = (x, y, (x + fruit_size[0]), (y + fruit_size[1]))

fruit = fruit.resize(fruit_size)
bg.paste(fruit, fruit_box, fruit)

img_path = os.path.join('.', 'output', 'png_paste.png')
bg.save(img_path)
print('保存成功 at {}'.format(img_path))

# GUI环境可以使用下面方式直接预览
bg.show()