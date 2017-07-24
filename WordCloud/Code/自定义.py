from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fh = open("E:\\文学\\天局.txt",'r')
text = fh.read()
fenci = " ".join(jieba.cut(text))

backgroud_Image = np.array(Image.open("F:\\Python\\procedure\\词云\\materials\\alice_color.png"))

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("仿佛")

wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,      # 设置背景图片
                stopwords = STOPWORDS,        # 设置停用词
                font_path = 'C:\\Windows\\Fonts\\simkai.ttf',# 设置字体格式，如不设置显示不了中文
                )
wc.generate(fenci)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()