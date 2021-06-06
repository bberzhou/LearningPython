#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image,ImageFilter
"""
	PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
	由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow
"""

# 通常的图像缩放操作
im = Image.open('test.png')

# 获取图像尺寸
w, h = im.size
print('Original image to :%s x %s' % (w, h))

# 缩放到50%
#
# im.thumbnail((w//2, h//2))
# print('Resize image to: %sx%s' % (w//2, h//2))
# im.save('test1.png', 'png')

# 对图片进行模糊
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('test2.png','png')

