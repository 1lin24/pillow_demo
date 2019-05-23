# coding=utf-8

"""
demo 制作一张圆形的头像

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
bg = Image.new('RGB', bg_size, color=(255,255,255))

avatar_size = (200, 200)
avatar_path = os.path.join('.', 'imgs', 'avatar.jpeg')
avatar = Image.open(avatar_path).convert('RGBA')
avatar = avatar.resize(avatar_size)

mask = Image.new('RGBA', avatar_size, color=(0,0,0,0))
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((0,0, avatar_size[0], avatar_size[1]), fill=(0,0,0,255))

x, y = int((bg_size[0]-avatar_size[0])/2), int((bg_size[1]-avatar_size[1])/2)
box = (x, y, (x + avatar_size[0]), (y + avatar_size[1]))
bg.paste(avatar, box, mask)

img_path = os.path.join('.', 'output', 'round_avatar.jpg')
bg.save(img_path)
print('保存成功 at {}'.format(img_path))

# GUI环境可以使用下面方式直接预览
# bg.show()
