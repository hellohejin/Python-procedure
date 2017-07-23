#验证码：为了防止暴力破解 爬虫模拟登陆 各种键盘钩子进行登陆
#验证码的干扰机制：1、背景点或线条 2、文字扭曲
#RGB色彩值：红、绿、蓝 取值（0-255）
#(255,255,255,0.1) 第四个参数一般是透明度
#图片的扭曲方式：水平(缩放、倾斜、位移) 垂直(缩放、倾斜、位移)

import random
import string
from PIL import Image,ImageDraw,ImageFont,ImageFilter

#Image:负责处理图片
#ImageDraw:负责处理画笔
#ImageFont:负责处理字体
#ImageFilter:负责处理滤镜

#项目步骤
    #1、定义一张图片
img = Image.new("RGB",(150,50),(255,255,255))
'''颜色模式、图片大小、图片颜色'''
    #2、创建画笔
draw = ImageDraw.Draw(img)
    #3、绘制线条和点
        #绘制线
for i in range(random.randint(1,10)):
    draw.line(
        #每条线有2个点确定，每个点有x,y值确定
        [
            (random.randint(1,150),random.randint(1,50)),
            (random.randint(1,150),random.randint(1,50))
        ],
        fill=(0,0,0)
    )
        #绘制点
for i in range(1000):
    draw.point(
        [
            random.randint(1,150),
            random.randint(1,150)
        ],
        fill=(0,0,0)
    )
    #4、绘制文字
        #文字随机产生
        #文字个数一定
#font_list = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
font_list = string.ascii_letters
c_chars = "".join(random.sample(font_list,4))
#字体
font = ImageFont.truetype("simsun.ttc",33)
draw.text((5,5),c_chars,font=font,fill="red")
'''文字位置(距离上和左)、文字内容、字体、文本颜色'''
    #5、定义扭曲参数
params = [
    1 - float(random.randint(1,2)/100),
    0,
    0,
    0,
    1 - float(random.randint(1, 2) / 100),
    float(random.randint(1, 2) / 500),
    0.001,
    float(random.randint(1, 2) / 500)
]
    #6、使用滤镜、添加滤镜
img = img.transform((150,50),Image.PERSPECTIVE,params)
'''扭曲范围、扭曲样式，扭曲参数'''

#进行扭曲
img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
img.save("f:/1.png")
img.show()
