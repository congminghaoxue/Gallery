#!/usr/bin/env python
# encoding: utf-8

import os
from os import listdir
from io import open
from os.path import isfile, join
import tinify
from PIL import Image
def ResizeImage(filein, fileout, width=85, height=85, type='jpg'):
    '''
    filein:  输入图片
    fileout: 输出图片
    width: 输出图片宽度
    height:输出图片高度
    type:输出图片类型（png, gif, jpeg...）
    '''
    img = Image.open(filein)
    out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
    out.save(fileout)

tinify.key='mucDYQ0aZYjgXiNT3KQ1WXRTG9pSzU06'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
photos_dir = os.path.join(BASE_DIR, 'photos')
thumbs_dir = os.path.join(BASE_DIR, 'thumbs')
opt_dir = os.path.join(BASE_DIR, 'optmized')
jsonstr='var result={"photos":{"photo":['
for f in listdir(photos_dir):
    p_path = join(photos_dir, f)
    t_path = join(thumbs_dir, f)
    o_path = join(opt_dir, f)
    if isfile(p_path):
        source = tinify.from_file(p_path)
        if not isfile(t_path):
            # ResizeImage(p_path, t_path)
            resized = source.resize(
                method="fit",
                width=85,
                height=85
            )
            resized.to_file(t_path)
        if not isfile(o_path):
            source.to_file(o_path)
        jsonstr+='{"thumb":"thumbs/' + f + '","url":"optmized/' + f + '","title":""},'
jsonstr = jsonstr[:-1]
jsonstr+=']}};'
with open(os.path.join(BASE_DIR, 'gallery.js'), "wb") as outfile:
    outfile.write(jsonstr)
