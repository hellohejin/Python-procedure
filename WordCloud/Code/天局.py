
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt

fh = open("E:\\文学\\天局.txt",'r')
text = fh.read()
fenci = " ".join(jieba.cut(text))
#print(text)
#print(fenci)

wordcloud = WordCloud(font_path="C:\\Windows\\Fonts\\simkai.ttf",
                      background_color="white",
                      max_words=80,
                      width=1000,
                      height=860, margin=2).generate(fenci)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()


