from wordcloud import WordCloud

f = open(u"F:\\Python\\procedure\\词云\\materials\\alice.txt",'r').read()
wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)

# width,height,margin(边缘)可以设置图片属性

# generate 可以对全部文本进行自动分词,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
#wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集

#background_color参数为设置背景颜色,默认颜色为黑色

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

wordcloud.to_file('F:\\Python\\procedure\\词云\\materials\\test.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存