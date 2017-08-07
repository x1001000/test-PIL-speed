N =100

from PIL import Image
from random import randint
from time import strftime
with Image.open('ufo_960x480.png') as fg:
    print('開始: ', strftime('%X'))
    for i in range(N):
        with Image.open('big_3840x2160.jpg') as bg:
            bg_w, bg_h = bg.size
            fg_w, fg_h = fg.size
            offset = (randint(0,bg_w)-fg_w//2, randint(0,bg_h)-fg_h//2)
            bg.paste(fg, offset, fg)
            bg.save('OUT-'+str(i)+'.jpg')
    print('結束: ', strftime('%X'))