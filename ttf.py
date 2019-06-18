# Copyright 2019 Anthony L. Leotta
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.


import os
from PIL import Image, ImageDraw, ImageFont
import random
 
# allowable_characters = 'ABCDFGHJKLMNPQRSTVWXYZ['
allowable_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# ~!@#$%^&*()-_=+,<.>;:[]{}|<<>>?"
# "ALCHEM__.TTF"

def random_word(allowable_characters, length):
    word=[]
    i=0
    
    while i<length:
        num = random.randint(0, len(allowable_characters))
        #print(num)
        word.append(allowable_characters[num-1])
        i+=1

    word = ''.join(word)

    return word

def generate_random_words(amount, fontpath, fontname):
    i=0
    font = ImageFont.truetype(os.path.join(fontpath, fontname),72)
    #font = ImageFont.truetype(fontname,72)
    while i<amount:
        text = random_word(allowable_characters,3)
        w, h = font.getsize(text)
        print(text, w,h)
        if w>0:
            img = Image.new('RGB', (w, h), color = (73, 109, 137))

            d = ImageDraw.Draw(img)
            d.text((0,0), text, fill=(255,255,0),font=font)

            img.save(os.path.join('words', filename[:-4] + '-' + text + '.png'))
        i+=1

def get_font_filenames(path):
    files = []
    # r=root, d=directories, f = files
    for path, d, f in os.walk(path):
        for file in f:
            if '.ttf' in file:
                files.append((path, file))                
    return files

fonts = get_font_filenames("fonts")    
# fonts = ['ASTROL.TTF']

# item is a tuple of path and filename
for item in fonts:
    (fontpath, filename) = item
    print(filename[:-4])
    generate_random_words(5, fontpath, filename)


