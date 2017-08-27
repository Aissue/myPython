import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('C:/Users/Public/Documents/python/result.txt', 'rb').read()
font = 'C:/Users/Public/Documents/python/font/simfang.ttf'

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud(collocations=False, font_path=font, width=2000, height=2000, margin=2).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()